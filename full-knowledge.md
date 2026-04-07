# HCSN Unified Knowledge File

Last updated: 2026-03-31 (Asia/Kolkata)
Workspace root: `/home/saif/antigravity`
Author/maintainer context: Saif Mukhtar (as documented in repo metadata)

## 0) Scope Of This File

This file is a consolidated, high-detail knowledge reference across the three active repositories in this workspace:

1. `test-hcsn-theory` (theory/docs + website)
2. `test-hcsn-sim` (Python simulation engine + experiments)
3. `hcsn-rust` (Rust high-performance implementation + hypothesis experiments)

It includes:
- canonical theory definitions and formulas
- lock-folder concepts (now included for knowledge synthesis)
- simulation architecture (Python + Rust)
- dataset status and observed numerical outputs present in workspace files
- operational meaning of symbols/observables
- external links used by the project

Important interpretation convention used here:
- `Canonical`: definitions from `test-hcsn-theory/docs/01..04`.

Per user instruction history in this workspace context, `Phase/Plan 10` details are intentionally not used as a core knowledge target.

---

## 1) External Links And Project Identity

Primary links used across repos:
- DOI (paper): https://doi.org/10.55277/researchhub.fvahxvpt.1
- YouTube overview: https://youtu.be/A0oh6Rlx03Y
- ORCID: https://orcid.org/0009-0004-1698-5729

Repository links referenced in docs/README:
- Theory repo (public reference): https://github.com/hcsn-theory/HCSN-core-Theory
- Simulation repo (public reference): https://github.com/hcsn-theory/hcsn-sim
- Org/contact: https://github.com/hcsn-theory

Website config placeholders currently present in theory website code:
- `https://hcsn-theory.research`
- `https://github.com/yourusername/hcsn-theory`
- `saifmukhtar@hcsn.tech`

---

## 2) Repository Roles In This Workspace

### 2.1 `thcsn-theory`
Purpose:
- Canonical conceptual framework, terminology discipline, boundaries, falsifiability, and open problems.
- Includes a Next.js website that renders docs from `../docs`.

Key canonical docs:
- `docs/01_axioms_and_methodology.md`
- `docs/02_defects_worldlines_and_particles.md`
- `docs/03_emergent_dynamics_momentum_and_interaction.md`
- `docs/04_geometry_dimension_uncertainty_and_limits.md`

### 2.2 `hcsn-sim`
Purpose:
- Python simulation and experiment stack (baseline/reference implementation).

Core modules:
- `engine/hypergraph.py`
- `engine/rules.py`
- `engine/rewrite_engine.py`
- `engine/observables.py`

Experiment/analysis:
- `sim-exp/*` (runs, measurements, plots, tests)
- outputs in `sim-exp/json/*`
- multiverse variants in `multiverse/*`

### 2.3 `hcsn-rust`
Purpose:
- Rust implementation for performance and large-scale emergence probing.
- Includes integrated hypothesis machinery (knot detection, survival memory, interaction event tracking).

Core modules:
- `src/hypergraph.rs`
- `src/rules.rs`
- `src/rewrite_engine.rs`
- `src/observables.rs`
- binaries in `src/bin/*`
- hypothesis log: `hypotheses/emergence_log.md`
- outputs in `exports/*`

---

## 3) Canonical Theory Core (Current Stable Baseline)

Source basis: theory docs 01-04.

### 3.1 Axiomatic substrate
The universe is modeled as a discrete causal hypergraph:
- vertices = events
- directed relations/hyperedges = causal structure
- rewrites = local evolution

No assumed:
- background manifold
- predefined metric
- external global time
- pre-imposed QM/field structures

### 3.2 Causality and time
- Causal consistency produces DAG-like ordering (no closed causal loops).
- Time is operationally rewrite depth, not an external clock.

### 3.3 Hierarchial Closure (`Ω`)
- Hierarchical Closure 2 is a coarse-grained, multi-scale statistical observable. It is computed after rewrite steps from the hypergraph's local motif structure, using the algorithm below. does not participate in the rewrite dynamics; it has no update equation, no causal continuity, and does not transport information. All rewrite decisions depend only on local structural quantities (coherence, density, memory) that are defined strictly within the hypergraph.

##### Precise Algorithmic Definition of Ω (added to Symbol Glossary and Section 10):

1. Interaction Graph: From the hypergraph  `H = (V,E)` , construct an undirected adjacency graph  `G`  where vertices are connected if they share a hyperedge (causal interaction).
2. Local Closure at Scale  r : For each vertex  `v` , consider its  r -neighborhood  `N_r(v)`  in  `G` .
   `C_r(v) = \frac{\text{number of closed motifs of size ≤ 3 within } N_r(v)}`
                `{\text{number of possible motifs of same size}}`
   (Implemented as a normalized clustering coefficient aggregated over triangles and 3-vertex motifs.)
3. Multi‑scale Closure: Weighted sum over small radii (e.g.,  r = 1,2 ):
   `\Omega = \frac{1}{|V|} \sum_{v \in V} \sum_{r=1}^{2} w_r \, C_r(v)`
   with  w_1 = 0.7, w_2 = 0.3  (example weights).
4. Properties:
   · Purely derived from current graph topology.
   · Re‑computed from scratch each time step.
   · No evolution equation, no propagation.


### 3.4 Emergent objects and identity
Operational chain:
- xi-cluster -> proto-object -> proto-particle (when criteria satisfied)

Identity via overlap continuity:

`|C(t) ∩ C(t+1)| / |C(t) ∪ C(t+1)| >= alpha`

### 3.5 Momentum, mass, interaction
Canonical momentum idea: persistent rewrite imbalance.

Mass proxy (canonical):

`m ~ 1 / Var(p)`

Interaction (canonical mechanism): rewrite competition for shared rewrite access, environment-mediated, statistically asymmetric and non-conservative at micro-level.

Interaction-strength proxy used in docs:

`F_AB = |Phi_A - Phi_B| / tau_coexist`

where `Phi` is rewrite flux, `tau_coexist` coexistence duration.

### 3.6 Geometry and dimension
Geometry is emergent and incomplete (current state).

Effective dimension definition:

`D_eff(r) = d log N(r) / d log r`

Canonical correction:
- average coordination `<k>` is not itself dimension.

### 3.7 Canonical phase structure
By Ω regime (canonical summary):
- Subcritical (`Ω < 1.0`): transient defects, no stable transport
- Critical (`Ω ~ 1.1`): marginal stability
- Supercritical (`Ω > 1.2`): persistent structures and stable transport signatures

### 3.8 Canonical uncertainty/lifetime relation
Empirical relation documented:

`Var(p) ~ tau^(-1)`

---

## 4) Symbol Glossary (Used Across Docs/Code)

- `H = (V,E)`: hypergraph
- `Ω` (Omega): hierarchical closure order parameter
- `ξ` (xi): transport activity/accounting scalar used in simulations
- `Φ` (Phi): rewrite flux (cluster or local rewrite-touch counts)
- `Ψ` (Psi): closure density observable
- `tau (τ)`: lifetime/persistence duration in rewrite steps
- `<k>`: average coordination/degree-like connectivity measure
- `L`: max causal chain length (depth)
- `d_AB`: overlap-based interaction distance proxy
- `m`: emergent mass proxy (operational/statistical)
- `p`: momentum proxy from rewrite persistence/asymmetry

---

## 5) Deprecated / Archived Material

- Earlier exploratory documents (previously in docs/lock) have been archived and are not part of the current canonical theory.
  They contained speculative extensions that are either superseded by the canonical docs or are now considered outdated. For the definitive HCSN formulation, refer to Sections 2-4 and the

simulation results.


## 6) Python Simulation Architecture (`test-hcsn-sim`)

### 6.1 Data model
- `Vertex`: id, depth, label (+1/-1)
- `Hyperedge`: k-ary relation
- `Hypergraph`: vertices, hyperedges, causal_order

### 6.2 Rewrite rules
- `edge_creation_rule`
- `vertex_fusion_rule`

### 6.3 Engine behavior (current Python baseline)
`engine/rewrite_engine.py` focuses on:
- rewrite proposal + acceptance
- ξ inheritance + ξ propagation
- cluster geometry memories
- forced probes (defect injections)

This baseline is more ξ-centric and does not include the full knot-memory mechanics that are deeply integrated in Rust.

### 6.4 Observables module
- worldline interaction graph
- interaction concentration `Φ`
- closure density `Ψ`
- hierarchical closure `Ω`
- Myrheim-Meyer dimension estimator
- coarse-graining helpers

### 6.5 Main experiment runner
`sim-exp/run_simulation.py` logs:
- time
- vertex count
- `<k>`, `L`, `Φ`, `Ψ`, `Ω`
- defects and rewrite history

---

## 7) Rust Simulation Architecture (`hcsn-rust`)

Rust implementation contains both parity components and additional in-engine emergence mechanics.

### 7.1 Core structures
- `Hypergraph` with vertex labels and causal order
- explicit `UndoRecord` for reversible rewrite proposals

### 7.2 Engine-level emergence machinery
In `src/rewrite_engine.rs`:
- candidate knot detection from local neighborhood coherence
- active/dead knot tracking
- overlap continuity matching
- stability memory per vertex (decay + accumulation + cap)
- coherence/density/memory-modulated suppression logic
- growth gating and boundary tension
- interaction event capture between overlapping knots

### 7.3 Key operational expressions implemented in Rust
Representative forms in engine logic:

- coherence from internal/boundary edges
- suppression term based on effective alpha:

  `alpha_eff = alpha_base + coherence_boost + memory_contribution`

- suppression probability with local density:

  `rewrite_prob = exp(-(alpha_eff * coupling_modifier) * local_density)`

- growth gating:

  `growth = beta if coherence > theta else 0`

- boundary tension term:

  `boundary_term = 1 / (1 + gamma * boundary_ratio)`

- knot mass proxy used in code:

  `mass = size * coherence^2`

- momentum proxy used in code:

  `momentum = mass * velocity_avg_x`

### 7.4 Rust run outputs
`src/bin/run_simulation.rs` exports:
- `exports/particle_lifetimes_p{p}_s{seed}.json`
- `exports/interaction_events_p{p}_s{seed}.json`

and marks particle-candidate flag using:
- `age >= tau_c` (tau_c set to 1000 in current run binary)
- `coherence > 1.0`

---

## 8) Hypothesis Evolution In Rust (`hypotheses/emergence_log.md`)

The emergence log documents a staged hypothesis progression (1-9) from rejected/flawed starts to richer survival/interaction regimes.

High-level sequence:
1. Local-curvature anomaly idea (rejected)
2. Fusion condensation bookkeeping idea (flawed)
3. Temporal knot criteria formulation
4. Density-dependent suppression tests
5. Suppression + growth + boundary tension formulation
6. Structure-gated nucleation breakthrough
7. Coherence-enhanced survival
8. Memory-based survival and tail behavior shift
9. Regime mapping and empirical interaction-law extraction

Frequently reported motifs:
- nucleation threshold concept (`tau_c`)
- hazard-rate reduction with survival reinforcement
- tail-law fitting (exponential vs power-law regimes)
- interaction-channel classification (pass-through/fusion/deflection/annihilation)

Knowledge-note boundary:
- treat quantitative fit values as run-dependent empirical summaries, not closed-form final laws.

---

## 9) Data Snapshot Present In Workspace

### 9.1 Python JSON outputs (`test-hcsn-sim/sim-exp/json`)
Notable current files include:
- `lorentz_cone.json`
- `effective_eom.json`
- `omega_c_by_variant.json`
- `particle_stats.json`
- `forced_probe_*.json`
- `timeseries.json`

Example values currently present:
- `lorentz_cone.json`: `violations: 0`
- `effective_eom.json`: `c_omega_sq`, `m_omega_sq`, `r_squared`
- `omega_c_by_variant.json`: multiple run entries with varying `Omega_c`

### 9.2 Python multiverse variants
`multiverse/baseline` and `variant_1..4` contain summarized outputs (`effective_eom.json`, `lorentz_cone.json`, `particle_stats.json`, `signal_speeds.npy`).

### 9.3 Rust exports snapshot
Current export directory includes many regime runs (`p=0.60..0.68` etc.) and at least one seed-specific deep run.

Observed summary from current files (workspace extraction):
- low/edge regimes (`p=0.45,0.50,0.55,0.70`) show 0 exported worldlines in those files
- active emergence window in mid-range (`~0.60-0.68`)
- seed-specific deep run file `particle_lifetimes_p0.64_s1.json` shows high persistence and large candidate count

---

## 10) Major Mathematical Relations Catalog

This section compiles formulas used across canonical docs, lock docs, and implementation narratives.

### 10.1 Substrate and evolution
- `H = (V, E)`
- `R_i: H -> H` (local rewrite)
- rewrite flow: `H_0 -> H_1 -> H_2 -> ...`
- time: `t := number of rewrites`

### 10.2 Defects and closure
- defect criterion: `|Delta Omega(t)| > epsilon`
- defect charge: `Q_defect := Delta Omega`

### 10.3 Continuity and identity
- overlap continuity:

  `|C(t) ∩ C(t+1)| / |C(t) ∪ C(t+1)| >= alpha`

### 10.4 Momentum/mass proxies
- canonical mass proxy: `m ~ 1 / Var(p)`
- empirical scaling relation: `Var(p) ~ tau^(-1)`
- code-level knot mass: `m = size * coherence^2`

### 10.5 Interaction proxies
- flux imbalance strength:

  `F_AB = |Phi_A - Phi_B| / tau_coexist`

- overlap distance proxy:

  `d_AB = 1 - |R_A ∩ R_B| / |R_A ∪ R_B|`

- lock rewrite pressure:

  `P_C = Phi_boundary(C)/|boundary(C)|`

### 10.6 Dimension and geometry
- effective dimension:

  `D_eff(r) = d log N(r) / d log r`

- lock effective interval expression:

  `ds^2 = c^2 d tau^2 - d ell^2`

### 10.7 Exploratory probability reinterpretation
- frequency-based outcome measure:

  `P(A) = lim_{N->∞} N(A)/sum_B N(B)`

---

## 11) Falsifiability And Open Problems

### 11.1 Canonical failure conditions (core)
Theory fails if (canonical criteria):
- no universal/finite emergent signal speed
- causal consistency breaks under evolution
- no persistent structures form
- universality absent across rule variations

### 11.2 Canonical open problems (current)
- dimensional selection mechanism
- emergent symmetry structure
- defect species classification
- distinct statistics classes
- exact invariance emergence in large-scale limit
- coarse-grained mapping to wider physical balance laws

---

## 12) Practical Run/Use Guide

### 12.1 Theory website
From `test-hcsn-theory/website`:
- `npm install`
- `npm run dev`

### 12.2 Python simulation
From `test-hcsn-sim`:
- `pip install -r requirements.txt`
- run main: `python3 sim-exp/run_simulation.py`
- many dedicated experiments under `sim-exp/*`

### 12.3 Rust simulation
From `hcsn-rust`:
- `cargo run --bin run_simulation --release -- --steps <N> --p_create <P> --seed <S>`
- `cargo run --bin exp_critical_scan --release`
- `cargo run --bin interaction_experiment --release`

Note on scripts:
- some helper Python scripts in `hcsn-rust` expect older filename/flag patterns; check current `src/bin/run_simulation.rs` naming and CLI behavior before batch use.

---

## 13)  Knowledge Boundary

The canonical truth source is theory docs 01-04, simulation outputs, and reproducible engine behavior. Any earlier speculative hypotheses have been archived and are no longer part of the active framework.
---

## 14) Condensed One-Page Theory Statement

HCSN models reality as local rewrites on a causal hypergraph without assuming spacetime as fundamental. Time is rewrite depth; persistent defect structures can emerge as worldline-like objects; momentum, mass, and interaction are operational rewrite-statistics quantities rather than primitive geometric forces. The order parameter Ω organizes regime behavior (subcritical/critical/supercritical), while ξ-activity and rewrite competition provide the practical channel for transport and interaction signatures in current simulations. Geometry and dimension are treated as emergent large-scale reconstructions, not assumed inputs, and remain incomplete/active research areas. The framework is explicitly falsifiable and organized around measurable simulation observables rather than external postulated structures.

