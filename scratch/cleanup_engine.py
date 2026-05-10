import sys

def cleanup():
    with open('hcsn-rust/src/rewrite_engine.rs', 'r') as f:
        lines = f.readlines()
    
    out = []
    skip_until = None
    
    for i, line in enumerate(lines):
        # 1. Remove cached_inter and interaction_counts fields from struct
        if 'pub cached_inter:' in line or 'pub interaction_counts:' in line:
            continue
        
        # 2. Remove from new()
        if 'cached_inter: None,' in line or 'interaction_counts: HashMap::new(),' in line:
            continue
            
        # 3. Handle step() method cleanup
        if 'let mut inter =' in line or 'self.cached_inter =' in line:
            continue
            
        # 4. Remove arguments from method calls
        line = line.replace('(&inter)', '()')
        line = line.replace('(inter)', '()')
        line = line.replace('(&self.h, inter,', '(&self.h,')
        line = line.replace('(h, inter,', '(h,')
        line = line.replace('(&knot_a.vertices, _inter)', '(&knot_a.vertices, &self.h)')
        line = line.replace('(&knot_b.vertices, _inter)', '(&knot_b.vertices, &self.h)')
        line = line.replace('(&ka.vertices, _inter)', '(&ka.vertices, &self.h)')
        line = line.replace('(&kb.vertices, _inter)', '(&kb.vertices, &self.h)')
        line = line.replace('(_inter, halo)', '(&self.h, halo)')
        
        # 5. Fix signatures
        if 'fn update_stability(&mut self,' in line:
            line = '    fn update_stability(&mut self) {\n'
        if 'fn perform_kinematics_and_interactions(&mut self,' in line:
            line = '    fn perform_kinematics_and_interactions(&mut self) {\n'
        if 'fn record_xi_current(&mut self,' in line:
            line = '    fn record_xi_current(&mut self) {\n'
        if 'pub fn propose_rewrite(&mut self,' in line:
            line = '    pub fn propose_rewrite(&mut self) -> Option<UndoRecord> {\n'

        out.append(line)
        
    with open('hcsn-rust/src/rewrite_engine.rs', 'w') as f:
        f.writelines(out)

cleanup()
