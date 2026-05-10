# HCSN Complete Reference — Unified Technical Guide

**Version:** Phase 12 (Refined)  
**Scope:** Theory + Code + Architecture + FAQ  
**Scale:** All results at ≤250k steps, ≤5k vertices unless noted

---

# PART A — THEORETICAL FOUNDATION

## Chapter 1: The Five Axioms

### Axiom 0 — Discrete Relational Substrate
The fundamental structure is a finite (but unbounded) hypergraph H = (V, E):
- Vertices = discrete events
- Hyperedges = causal relations
- Partial causal ordering ⪯ relates events
- NO background manifold, metric, coordinates, or embedding space
- **Mach's Principle:** Motion and position are purely relational (interaction-dependent)

### Axiom 1 — Causal Consistency
The causal relation ⪯ satisfies:
1. **Irreflexivity:** ∀e, ¬(e ⪯ e) — no event causes itself
2. **Transitivity:** (e₁ ⪯ e₂ ∧ e₂ ⪯ e₃) ⇒ e₁ ⪯ e₃

**Proof of DAG:** Suppose a cycle a ⪯ b ⪯ ... ⪯ a. By transitivity: a ⪯ a. Contradiction with irreflexivity. ∎

### Axiom 2 — Local Rewrite Dynamics
Evolution = local probabilistic rewrites on bounded subgraphs. Each rewrite:
- Acts on bounded neighborhood only
- Modifies finite information
- Preserves causal consistency
- No global references or future dependencies

### Axiom 3 — Local Finiteness
Past(e) and Future(e) are finite for every event e.

### Axiom 4 — Hierarchical Closure Tension
Rewrite dynamics favor hierarchical closure (multi-scale causal consistency) while suppressing redundancy and hub dominance. A regulatory tension, not a maximization principle.

### Axiom 5 — Defect Permissibility
Localized violations of closure balance are allowed. These form the basis for emergent structure.

### What Is NOT Assumed
- Space, distance, dimension
- Time as external parameter
- Mass, energy, momentum, fields
- Hilbert spaces, state vectors, amplitudes
- Symmetry principles from external frameworks

---

## Chapter 2: Key Observables

### Ω — Hierarchical Closure (Order Parameter)
- Measures internal/boundary edge ratio of local neighborhoods
- **Classifies** phase regimes but does NOT **drive** transitions
- "Ω is a thermometer, not a heater"
- Computed by `compute_omega()` in `observables.rs`

| Ω Regime | Behavior | ξ Transport |
|:---------|:---------|:------------|
| Subcritical (< 1.0) | Transient defects, τ < 100 | None |
| Critical (≈ 1.1) | Marginal stability, τ ~ 10³–10⁴ | Power-law |
| Supercritical (> 1.2) | Persistent knots, τ > 10⁵ | Constant |

### ξ — Activity Tracer (Diagnostic)
- Scalar accounting variable tracking rewrite activity
- Does NOT feed back into rewrite dynamics
- Propagates via diffusion: 70% self-retention + 15%/degree to neighbors per step
- Half-life without reinforcement: ~1.4 steps
- **Not a physical field** — a passive tracer for diagnostics

### χ — Structural Overlap (Three Thresholds)

| Threshold | Value | Purpose |
|:----------|:------|:--------|
| Halo Contact | χ_rel > 0.015 | Begin tracking Relational InteractionEvent |
| Force onset | χ_rel > 0.14 | Empirical onset of momentum exchange |
| Deep coupling | χ_rel > 0.4 | Reduce core rewrite protection |

### Coherence — Internal/Boundary Edge Ratio
coherence = internal_edges / boundary_edges for a vertex neighborhood.
Used in: knot detection (threshold 1.2), suppression formula, mass calculation.

---

## Chapter 3: Particles and Identity

### What Is a Particle?
A particle (topological knot) is a coherent subgraph that:
1. **Persists** — lifetime τ >> local rewrite correlation time
2. **Has momentum coherence** — bounded rewrite imbalance variance
3. **Has inertial stability** — lifetime scales with 1/Var(p)
4. **Structurally couples** — stability correlates with Ω

### Identity Through Overlap Continuity
Two clusters C(t) and C(t+1) are the same particle if:
```
|C(t) ∩ C(t+1)| / min(|C(t)|, |C(t+1)|) ≥ 0.3
```
Particles are *what the network remembers*, not what it contains.

### Detection Algorithm
1. For each vertex: compute 1-hop neighborhood coherence
2. If coherence ≥ 1.2 AND compactness ≥ 0.6: candidate seed
3. Union-Find merge candidates sharing > 30% vertices
4. Match to existing knots by overlap; unmatched = new birth or death

---

## Chapter 4: Mass, Momentum, and Dynamics

### Mass — Two Candidate Definitions

| Definition | Formula | Status |
|:-----------|:--------|:-------|
| Theoretical | m ~ 1/Var(p) | Aspiration, not yet validated |
| Code implementation | m = |V| × C² | Active in simulation |

Equivalence is an **open question**.

### Momentum
Statistical persistence of rewrite imbalance. Three correlated measures (not proven equivalent):
1. Before/after rewrite asymmetry
2. Inverse variance of causal displacement
3. Rewrite flux autocorrelation

### Relational Kinematics (The Machian Solution)
HCSN abandons absolute coordinates. All kinematic properties exist only *between* interacting structures.

**1. Relational Distance ($d_{AB}$):**
Defined by **Halo-Overlap** ($\chi_{rel}$). The Halo is the 1-hop structural expansion of the knot. This solves the "Horizon Problem" allowing approach-sensing before core contact.

**2. Relational Velocity ($v_{rel}$):**
Instantaneous rate of change of structural overlap: $v_{rel} = d\chi/dt$.
To filter rewrite noise, an **Exponential Moving Average (EMA)** is used:
`v_smoothed = (0.2 * v_raw) + (0.8 * v_smoothed)`

**3. Relational Momentum ($p_{rel}$):**
$p_{rel} = m_{reduced} \times v_{rel\_smoothed}$

**4. The 1D Relational Regime:**
Current kinematics are **scalar-only**. Because the emergent dimensionality ($D$) of the HCSN universe is not yet proven, we avoid ad-hoc coordinate systems. 
- **Consequence:** Scattering angles ($\theta$) and momentum vectors are currently **undefined**.
- **Status:** We track collision *intensity* and *scalar conservation*, not geometric deflection.

**Note on Absolute Proxies:** Diagnostic proxies (like vertex-ID centroids) are still used for visualization but are deprecated for physics. Absolute velocity for a single particle is undefined in the HCSN universe.

---

## Chapter 5: Interaction and Force

### Interaction = Competitive Rewrite Access
Two particles interact when their **Halos** share vertices ($\chi_{rel} > 0.015$). This interaction is:
- **Relational:** Defined only by the pair's joint state.
- **Short-Range:** 1-hop halos create a **Yukawa-like potential** (nuclear-like force).
- **Environment-mediated:** via Ω-modulated rewrite pool.
- **Asymptotically Free (Phase 14):** Suppression factor $\alpha_{eff}$ liquefies during deep overlap ($\chi \ge 0.4$), allowing fluid movement.

### Empirical Scaling Relation
F ~ k/$\chi_{rel}$ (k = 182.1, fit to Phase 12 data)

This is a **phenomenological observation**, not a derived law. The constant k scales with the coupling between the 1-hop halo and the **Relational Relief** ($\Gamma$).

### Scattering
Mean deflection θ = 71.5° (back-scattering bias). Measured in Phase 12 data.

---

## Chapter 6: Conservation — Honest Assessment

### Unpatched Results (HCSN_PATCHES=false)
- Mean Spearman ρ = −0.47 ± 0.16 (9 seeds, 60k rewrites each)
- This is **weak-to-moderate** correlation (R² ≈ 0.22)
- NOT exact conservation — no Δp = 0 observed
- Worst-case seed: ρ = −0.24

### Patched Results (HCSN_PATCHES=true, default)
Three **engineered** corrections:
- **Pairwise (A):** Symmetric momentum redistribution, strength ramps with stability
- **FluxCompensated (C):** Momentum reservoir with diffusive re-absorption
- **StabilityScaled (B):** Inertial cooling via exp(−S/30)

### Key Open Question
Does ρ strengthen toward −1.0 at larger scales (>10⁶ vertices)?

---

## Chapter 7: Emergence Classification

| Property | Type | Mechanism | Mode |
|:---------|:-----|:----------|:-----|
| Coherent subgraph formation | **Emergent** | Base rules | Pure |
| Knot persistence (>50 steps) | **Emergent** | No memory needed | Pure |
| F ~ k/χ scaling | **Emergent** | All modes | Pure + Assisted |
| Power-law lifetimes | **Assisted** | Stability memory (H8) | Assisted |
| ρ ≈ −0.47 correlation | **Emergent (fragile)** | Unpatched | Baseline |
| Asymptotic Freedom | **Emergent Analogue** | Relational Relief Function | Hybrid |
| Stronger conservation | **Engineered** | Hybrid patches | Hybrid |

**Definitions:**
- **Emergent:** Arises from base rules without designed mechanisms
- **Assisted:** Requires memory/feedback but not direct correction
- **Engineered:** Requires explicit correction patches

---

# PART B — CODE ARCHITECTURE

## Chapter 8: Axiom-to-Code Mapping

| Axiom | Code | File |
|:------|:-----|:-----|
| Axiom 0 (Hypergraph) | `Hypergraph` struct: `vertices`, `hyperedges`, `causal_future/past` | `hypergraph.rs` |
| Axiom 1 (Causal DAG) | `add_causal_relation()` + `FixedBitSet` transitive closure | `hypergraph.rs` |
| Axiom 2 (Local rewrites) | `edge_creation_rule()`, `vertex_fusion_rule()` | `rules.rs` |
| Axiom 3 (Finite cones) | `FixedBitSet` cap 524,288; `scrub_ghost_bits()` | `hypergraph.rs` |
| Axiom 4 (Closure tension) | `propose_rewrite()`: `prob = exp(−α_eff × density)` | `rewrite_engine.rs` |
| Axiom 5 (Defects) | No hard block on local Ω violations | `rewrite_engine.rs` |

## Chapter 9: File-by-File Guide

### `hypergraph.rs` — The Universe Data Structure
```
Vertex { id: u64, depth: usize, label: i8, parents: Vec, children: Vec }
Hyperedge { id: u64, vertices: Vec<u64> }
Hypergraph {
    vertices: HashMap<u64, Vertex>
    hyperedges: HashMap<u64, Hyperedge>
    causal_future: HashMap<u64, FixedBitSet>  // J+(v)
    causal_past: HashMap<u64, FixedBitSet>    // J-(v)
}
```
Key operations:
- `add_vertex()` — Atomic ID counter, creates empty bitsets
- `add_causal_relation(u, v)` — Updates bitsets transitively, O(N) worst case
- `scrub_ghost_bits()` — Cleans stale vertex references from bitsets

### `rules.rs` — The Two Rewrite Rules
- `edge_creation_rule()` — Birth: new vertex + causal links + loop closure (prob p_create)
- `vertex_fusion_rule()` — Contraction: merge two vertices, union causal histories
- Both return `UndoRecord` for reversibility

### `rewrite_engine.rs` — The Main Loop (1912 lines)
Core function: `step()` — see HCSN_SIMULATION_WORKFLOW.md for full execution order.
Key subsystems:
- Suppression formula: `exp(−((α_base + coherence_boost + memory_contribution) * coupling_modifier) × density)`
- Relational Relief: `coupling_modifier = 1.0 - 0.8 * min(1.0, chi/0.4)` (Asymptotic Freedom)
- Stability memory: decay × 0.975 + accumulate +1 per knot vertex, cap 50
- Knot tracking: detect → match → birth/death
- Kinematics: mass/velocity/momentum every 10 steps
- Conservation modes: Baseline, Pairwise, FluxCompensated, StabilityScaled, TimeSymmetry, Hybrid

### `observables.rs` — Measurement Instruments
- `compute_omega()` — Hierarchical closure (diagnostic only)
- `detect_candidate_knot_neighborhoods()` — Particle detection
- `compute_coherence_raw()` — Internal/boundary edge ratio
- `component_radius()` — Knot spatial extent
- `local_clustering()` — Clustering coefficient for suppression

### `persistence.rs` — Data Export
- CSV output via `BufWriter` wrapped in `Arc<Mutex<>>`
- NaN/Inf detection skips corrupt rows
- 21-column format per InteractionEvent

### `physics_params.rs` — Runtime Configuration
All parameters readable from environment variables:

| Env Var | Parameter | Default |
|:--------|:----------|:--------|
| HCSN_STEPS | total_steps | 250,000 |
| HCSN_P_CREATE | p_create | 0.58 |
| HCSN_NU | stability_decay | 0.975 |
| HCSN_GAMMA | nonlinear_coupling | 2.2 |
| HCSN_MU | memory_coupling | 0.3 |
| HCSN_PATCHES | enable_conservation_patches | true |
| HCSN_DEFECT_INJECTION | defect_injection | 0.0 |

### `main.rs` — Entry Point
1. Read env vars → 2. Create shared CSV writer (Arc+Mutex+BufWriter) → 3. Spawn 2 Rayon threads → 4. Each thread: seed Hypergraph → create RewriteEngine → loop step() → flush every 2000 steps

---

## Chapter 10: Key Constants (Memorize These)

| Constant | Value | Where |
|:---------|:------|:------|
| Interaction threshold | χ_c = 0.14 | Phase 12 data |
| Empirical coupling | k = 182.1 | Phase 12 fit |
| Mean deflection | θ = 71.5° | Phase 12 data |
| Stability decay | ν = 0.975 | physics_params.rs |
| Nonlinear coupling | γ = 2.2 | physics_params.rs |
| Memory coupling | μ = 0.3 | physics_params.rs |
| Suppression base | α_base = 2.0 | rewrite_engine.rs |
| Nucleation threshold | θ_nuc = 1.3 | rewrite_engine.rs |
| Growth boost | β = 1.5 | rewrite_engine.rs |
| ξ self-decay | 0.70 per step | rewrite_engine.rs |
| Bitset capacity | 524,288 (2¹⁹) | hypergraph.rs |
| Stability cap | 50.0 | rewrite_engine.rs |
| Conservation ρ | −0.47 ± 0.16 | v3.1 replication |
| Overlap identity | 30% threshold | process_knot_update |
| Coherence threshold | ≥ 1.2 | knot detection |
| History buffer | 200 undo records | rewrite_engine.rs |

---

# PART C — KNOWN LIMITATIONS & OPEN PROBLEMS

## Chapter 11: Honest Assessment of Limitations

### Critical Limitations
1. **Short-Range Only:** Current 1-hop halos only model nuclear-range interactions. Macroscopic 1/r² forces (Gravity) remain an open problem.
2. **Mass definition gap:** Theory says m ~ 1/Var(p), code uses m = |V|×C². No proof of equivalence.
3. **Scale ceiling:** All results at ≤250k steps. Asymptotic behavior unknown.

### Known Engineering Choices (Not Emergence)
1. Stability memory (H8) — designed positive feedback loop
2. coupling_modifier = 0.2 — hand-tuned parameter
3. Conservation patches (Hybrid mode) — explicit correction
4. Coherence threshold 1.3 — design parameter
5. Velocity clamp [-10, 10] — numerical safety band-aid

### Algorithmic Bottlenecks
1. `add_causal_relation()` — O(N) transitive closure update
2. `scrub_ghost_bits()` — O(V) cleanup every 100 steps
3. Hard-coded 2 threads (deliberate for dual-core study)

### What HCSN Does NOT Claim
- Reproduction of any known physical theory
- Derivation of Standard Model particle spectrum
- Exact conservation laws
- Quantum mechanics (no superposition, entanglement, or unitarity)
- Prediction of measurable physical quantities
- Correspondence to real spacetime geometry

---

## Chapter 12: Open Problems

### Theoretical
1. Dimensional selection mechanism (does D stabilize? at what value?)
2. Emergent symmetry structure from rewrite equivalence classes
3. Classification of stable defect species
4. Exact invariance principles in continuum limit
5. Connection to external physics frameworks

### Implementation
1. Proper metric embedding (graph geodesics, persistent homology)
2. Validate mass equivalence (1/Var(p) vs |V|×C²)
3. Scale to 10⁶+ vertices (requires dedicated hardware)
4. Parameter sensitivity analysis (systematic single-variable sweeps)
5. Automated ensemble runs with statistical confidence intervals

---

# PART D — FREQUENTLY ASKED QUESTIONS

## FAQ 1: What exactly is HCSN?
**A:** A discrete dynamical system simulator. It evolves a causal hypergraph via stochastic local rewrite rules and measures whether persistent, particle-like structures emerge. It is a computational framework for testing whether physics-like properties can arise from purely structural dynamics.

## FAQ 2: How is this different from Wolfram Physics?
**A:** Both use hypergraph rewriting, but HCSN: (1) uses rigorous operational measurement rather than observer theory, (2) implements stability memory for power-law lifetimes, (3) focuses on threshold-gated interaction rather than observer-dependent rules, (4) has a falsifiability framework built in. The closest cousin is actually Causal Set Theory (Sorkin), which shares the discrete-causal substrate.

## FAQ 3: Why Rust instead of Python?
**A:** The original Python engine (hcsn-sim) hit a hard wall at ~50k steps due to GIL limitations and O(N²) dictionary operations. Rust gave 50-100× speedup via: FixedBitSet for O(1) causal lookups, zero-cost abstractions, Rayon parallelism, and cache-friendly memory layout.

## FAQ 4: How do you measure velocity without space?
**A:** Via **Relational Kinematics**. We measure the rate of change of structural overlap ($\chi$) between interacting knots. Following Mach's Principle, absolute velocity for a single knot is undefined; we only track how fast knots are approaching or receding from each other.

## FAQ 5: Are the conservation laws real?
**A:** They are **emergent correlations**. In a background-independent universe, momentum exchange is the structural response to overlap change. Unpatched simulations show weak statistical correlation (ρ ≈ −0.47). The Hybrid mode adds engineered corrections. The open question is whether unpatched correlation strengthens at larger scales.

## FAQ 6: What does "emergent" actually mean here?
**A:** We classify results into three tiers: **Emergent** (arises from base rules alone, verified in Pure mode), **Assisted** (requires memory feedback but not direct correction), **Engineered** (requires explicit patches). See Chapter 7 for the full classification table.

## FAQ 7: Why do you need a workstation?
**A:** Current results are at ≤5k vertices. Key open questions (dimensional stabilization, conservation asymptotic behavior, large-scale universality) require 10⁶+ vertices. At O(N) per causal update and 10⁶ vertices, each step takes ~100ms. A 32-core workstation with 128GB RAM would enable ensemble runs across parameter space in reasonable time.

## FAQ 8: What would falsify HCSN?
**A:** Four criteria: (1) No universal signal speed emerges [PASSED], (2) Causal consistency breaks under evolution [PASSED], (3) No persistent structures form [PASSED], (4) Universality absent across rule variations [UNDER TEST].

## FAQ 9: Is this a theory of everything?
**A:** No. HCSN is a computational exploration of whether physics-like properties can emerge from discrete causal dynamics. It makes no claim to reproduce the Standard Model, derive coupling constants, or predict measurable quantities. It is a theory *in formation*, not a finished model.

## FAQ 10: What is the single strongest result?
**A:** That coherent, persistent subgraphs with power-law lifetime distributions emerge spontaneously from base rewrite rules. This is verified in Pure mode without any engineered mechanisms. The force scaling F ~ k/χ is also emergent across all modes.

## FAQ 11: What is the "Interaction Halo"?
**A:** It is a 1-hop structural expansion of a knot's vertices. By measuring the overlap of halos rather than just cores, we solve the **Horizon Problem**—knots can "sense" each other's approach before they physically collide. This creates a short-range interaction zone analogous to the Strong Nuclear Force.

## FAQ 12: How does the suppression formula work?
**A:** `rewrite_prob = exp(−α_eff × coupling_modifier × local_density)` where α_eff = 2.0 + coherence_boost + memory_contribution. High-density coherent regions with stability memory are exponentially hard to rewrite. This is the key mechanism for knot persistence.

## FAQ 13: What is the stability memory system?
**A:** Every 10 steps: (1) all stability values decay × 0.975, (2) vertices inside active knots gain +1.0 stability (cap 50). This creates a positive feedback loop: surviving vertices gain protection, making them harder to destroy, so they survive longer. This converts exponential decay to power-law survival.

## FAQ 14: What generates the 0.14 threshold?
**A:** It is an empirical observation from Phase 12 data, not a designed parameter. Below χ = 0.14, momentum exchange between interacting knots is statistically indistinguishable from noise. The threshold emerges from the interaction between suppression dynamics and overlap statistics.

## FAQ 15: How does hcsn-gantry relate to the simulation?
**A:** Gantry is the observability pipeline. It launches and monitors multiple simulation workers, collects telemetry (CPU, RAM, Ω, knots), stores it in SQLite, and serves a live dashboard. It does NOT affect simulation physics — it is purely monitoring infrastructure.

---

*End of HCSN Complete Reference — Unified Technical Guide*
*Companion documents: HCSN_SIMULATION_WORKFLOW.md (execution flow) · HCSN_ECOSYSTEM_GUIDE.md (all repos)*
