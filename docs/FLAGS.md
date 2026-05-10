# HCSN Engine Execution Flags

The `run_simulation` binary is fully parameterized, allowing you to tweak the underlying physics and macroscopic behavior of the hypergraph simulation directly from the command line without modifying the codebase.

## Usage
```bash
cargo run --release --bin run_simulation -- [FLAGS]
```

## Structural Growth Parameters
These parameters govern the raw structural generation and graph rewriting dynamics.

- `--steps <usize>`: Number of rewrite steps to simulate. (Default: `5000`)
- `--p_create <f64>`: Probability of creating an edge. Higher values bias the system toward expansive hypergraph growth. (Default: `0.85`)
- `--p_fusion <f64>`: Probability of fusing vertices. Because fusion deletes all hyperedges connected to a vertex, values > 0.15 typically cause network structural collapse or starvation. (Default: `0.10`)
- `--seed <u64>`: RNG seed for deterministic runs. (Default: `1`)

## Physics & Field Dynamics
These parameters tune the internal fields (Inertia, Coherence, Memory) that govern how Topological Knots emerge, interact, and survive.

- `--gamma <f64>` (Non-linear Coupling): Exponent governing how rapidly structural stability translates into "memory" or "protection" for a vertex. Higher values create sharp phase transitions where only highly stable knots survive. (Default: `2.2`)
- `--mu <f64>` (Memory Coupling): Coefficient determining the strength of the non-linear stability protection field. (Default: `0.3`)
- `--nu <f64>` (Stability Decay): The rate at which vertex stability degrades per cycle. Closer to 1.0 means infinite persistence, lower means rapid forgetting. (Default: `0.975`)
- `--gamma_defect <f64>`: Coupling strength for topological defects/perturbations. (Default: `0.15`)
- `--inertia_scale <f64>`: Multiplier applied to the calculated mass/momentum of emergent topological knots. (Default: `1.0`)
- `--interaction_boost <f64>`: Coherence multiplier applied during active interaction events between knots. (Default: `1.02`)

## Noise & Perturbations
- `--defect_injection <f64>`: Probability or rate of actively injecting topological defects into the vacuum to test the robustness of knot emergence. (Default: `0.0`)
- `--disable_patches`: Flag that completely disables the physics conservation constraints (momentum coupling, symmetric correction, etc.). Useful for testing baseline pure topology behavior.

## Execution Modes & Physics Pipelines

The simulation engine can be run in different modes that fundamentally alter how the hypergraph evolves. Understanding these modes is critical to predicting experimental behaviors.

### 1. The "Honest Physics" Mode (Default)
**Command:** `cargo run --release --bin run_simulation -- [FLAGS]` *(Running without `--pure`)*
- **How it works:** This is the full analytical physics pipeline. Before any rewrite (creation/fusion) occurs, the engine calculates the `local_density` and structural `coherence` of the target vertices.
- **The Density Filter:** If the structural density gets too high (e.g., vertices are tightly clustered into a dense hyperedge), an exponential density filter (`exp(-alpha_eff * local_density)`) aggressively suppresses further rewrites on those vertices to prevent runaway physical singularities.
- **Important Caveat:** If you start the simulation with a fully connected 4-vertex vacuum seed in this mode, the density filter calculates a massive suppression probability (`exp(-12) ≈ 99.9994% rejection`). The simulation will intentionally **stall** at 4 vertices because the initial state is mathematically deemed too dense to expand.

### 2. Pure Mode (`--pure`)
**Command:** `cargo run --release --bin run_simulation -- --pure [FLAGS]`
- **How it works:** The engine explicitly **bypasses** the density filter, coherence checks, and memory suppression algorithms.
- **Purpose:** This mode is used for raw, unobstructed structural emergence. The engine strictly relies on the raw `--p_create` and `--p_fusion` probabilities to randomly generate topology.
- **When to use it:** You must use this mode when initiating a simulation from tiny, dense vacuum seeds. Bypassing the density filter allows the graph to "inflate" and expand rapidly into a massive hypergraph before complex analytical physics take over.

### 3. Other Utility Modes
- **`--baseline`:** Disables expensive heuristic reporting (like complex causal interaction loop profiling) for significantly faster macroscopic simulation speeds.
- **`--aggressive_mode`:** Engages `EmergenceMode::Control`, forcing strict kinematic conservation constraints on the topological knots.
- **`--log-to <string>`:** Overrides the target file destination for the JSONL simulation event log.

---

### Example
Run a 100,000 step pure-mode simulation, forcing fusion to 5%, raising memory coupling to 0.5, and setting a specific deterministic seed:
```bash
cargo run --release --bin run_simulation -- --steps 100000 --pure --p_fusion 0.05 --mu 0.5 --seed 42
```
