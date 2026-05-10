import sys

def fix_engine():
    with open('hcsn-rust/src/rewrite_engine.rs', 'r') as f:
        lines = f.readlines()
    
    out = []
    in_impl = False
    
    # 1. First pass: remove the bad update_topological_knots and other junk
    cleaned = []
    for line in lines:
        if 'pub fn update_topological_knots(&mut self) {' in line and 'Self::process_knot_update_static' in lines[lines.index(line)+1]:
            # This is a bad insertion, skip it and its block
            continue
        # Skip lines that look like parts of the misplaced method
        if 'Self::process_knot_update_static(' in line and 'next_knot_id,' in lines[lines.index(line)+3]:
            continue
        cleaned.append(line)
        
    # 2. Second pass: correct scoping and signatures
    for i, line in enumerate(cleaned):
        # Fix u_idx scoping in xi propagation
        if 'for u_idx in neighbors.ones() {' in line:
            out.append(line)
            out.append('                    let u = u_idx as u64;\n')
            continue
        if 'let u = u_idx as u64;' in line: # skip misplaced ones
            continue
            
        # Fix Self:: to RewriteEngine:: if needed (but better to keep it in impl)
        
        # Ensure we are inside impl RewriteEngine for the new method
        if 'impl RewriteEngine {' in line:
            in_impl = True
            
        out.append(line)

    # 3. Insert update_topological_knots properly at the start of impl
    final_out = []
    method_added = False
    for line in out:
        final_out.append(line)
        if 'impl RewriteEngine {' in line and not method_added:
            final_out.append('\n    pub fn update_topological_knots(&mut self) {\n')
            final_out.append('        Self::process_knot_update_static(\n')
            final_out.append('            &self.h,\n')
            final_out.append('            &mut self.active_knots,\n')
            final_out.append('            &mut self.dead_knots,\n')
            final_out.append('            &mut self.next_knot_id,\n')
            final_out.append('            &self.stability,\n')
            final_out.append('            self.time,\n')
            final_out.append('            1.2,\n')
            final_out.append('            0.3,\n')
            final_out.append('        );\n')
            final_out.append('        self.perform_kinematics_and_interactions();\n')
            final_out.append('    }\n')
            method_added = True

    # 4. Remove the very last line if it is a duplicate }
    while final_out[-1].strip() == '}' and final_out[-2].strip() == '}':
        final_out.pop()

    with open('hcsn-rust/src/rewrite_engine.rs', 'w') as f:
        f.writelines(final_out)

fix_engine()
