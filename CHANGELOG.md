# Changelog: HCSN Nexus vs Legacy HCSN-Rust

This document outlines the critical architectural upgrades, bug fixes, and parameterization enhancements implemented in the `hcsn-nexus` engine compared to the legacy `hcsn-rust` codebase.

## 1. 🐛 Critical Bug Fixes

### The 15GB OOM Memory Leak
- **Issue**: The simulation was consuming gigabytes of RAM within minutes, eventually crashing the operating system.
- **Root Cause**: The `h.vertices.retain()` cleanup phase inside `rewrite_engine.rs` contained an infinite loop trap. As vertices were marked for deletion, they were not properly decoupled from the causal `interaction_graph` before removal, resulting in dangling pointers and infinite iteration cycles when calculating `local_density`.
- **Fix**: Implemented a strict O(1) topological cleanup pass that correctly zeroes out causal edges before popping vertices from the hashmap. The engine is now completely memory stable, remaining under 100MB even at 10,000+ vertices.

### The Topological Stalling (0.0% Acceptance Rate)
- **Issue**: The simulation would stall out at exactly 4 vertices and 1 edge, refusing to generate any new structures.
- **Root Cause**: The legacy engine relied heavily on the `--pure` flag to bypass the exponential density filter (`exp(-12)`) on the initial 4-vertex seed. However, the `run_simulation.rs` wrapper had a silent, hardcoded override block that forced `p_create = 0.45` and `p_fusion = 0.50` if `--pure` was passed. A 50% fusion rate hyper-destroys the graph, starving it of edges.
- **Fix**: Eradicated the silent overrides in `run_simulation.rs`. The engine now perfectly respects the production density target of `p_create = 0.64` and `p_fusion = 0.10` directly from the CLI.

## 2. ⚙️ Engine Modularization

### `EngineConfig` Architecture
- Abstracted all hardcoded physics parameters into a centralized `EngineConfig` struct.
- Allows direct command-line manipulation of core phenomena without requiring recompilation:
  - `--p_create` and `--p_fusion`
  - `--gamma` (Nonlinear memory coupling)
  - `--mu` (Memory stability strength)
  - `--nu` (Defect stability decay)
  - `--interaction_boost`

### Backward Compatibility via Builder Pattern
- Introduced `RewriteEngine::with_config(config)` for the production binary.
- Preserved the legacy `RewriteEngine::new()` constructor to ensure all 9 auxiliary analysis scripts (`phase_detection.rs`, `robustness_pipeline.rs`, etc.) continue compiling and functioning flawlessly without breaking changes.

## 3. 📈 Observables and I/O

- **Clean Terminal Output**: Aligned the simulation STDOUT table to track acceptance rate (`acc%`), vertex growth (`V`), and memory usage (`RSS_MB`) tightly and cleanly.
- **Graceful Interrupts**: Validated that hitting `Ctrl+C` correctly triggers the `SIGNAL` capture, finalizing the current topological step and securely exporting the dataset (e.g., `exports/particle_lifetimes_...json`) before exiting, preventing data corruption on long overnight runs.
