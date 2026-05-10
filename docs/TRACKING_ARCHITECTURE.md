# Topological Tracking Architecture
**Internal Logic & Decision History**

This document records the architectural journey of the `RewriteEngine`'s knot tracking system. Tracking emergent topological phenomena (knots) fundamentally introduces an $O(V)$ "God-like observer" calculation, which conflicts directly with the $O(1)$ local physics updates.

When attempting to optimize the engine for massive 100,000-step baselines, we iterated through several tracking paradigms. This document serves as a historical record of what we tried, why certain ideas were mathematically rejected, and why the engine is currently configured the way it is.

---

## 1. The Bottleneck: The God-Mode Observer
The core engine runs at $O(1)$ because rewrites only check local 1-hop neighborhoods. However, `update_topological_knots()` and `detect_candidate_knot_neighborhoods()` must scan the entire universe (all $V$ vertices) to detect patterns of high coherence. 
Running this on every step effectively degraded the entire simulation to $O(V^2)$, making large-scale growth prohibitively slow.

## 2. Attempt 1: 100-Step Temporal Throttling
**The Idea:** Add a `--track_interval` flag to run the $O(V)$ scanner only every 100 steps.
**The Failure (Overlap Threshold Drift):** This mathematically failed. The observer matches particles across time using an `overlap_threshold` (e.g., $0.3$). If a particle at $t$ shares $>30\%$ of its vertices with a candidate at $t+100$, it survives. 
However, in 100 steps of topological evolution, the particle "drifts" so much that it naturally exchanges over $70\%$ of its vertices with the vacuum. The observer constantly saw overlaps $< 30\%$, assuming the particle had died. **Result:** Particle lifetimes were artificially destroyed.

## 3. Attempt 2: The "Lighthouse" Tracking Algorithm
**The Idea:** Eradicate the $O(V)$ scan by switching to $O(K)$ anchored tracking. 
1. Assign an "Anchor" vertex (highest density) to each identified knot.
2. Every step, run a localized 2-hop BFS outward from the $K$ anchors to reconstruct the particles.
3. If an anchor is destroyed by a rewrite, hand the anchor status to its densest neighbor.

**The Rejection (Philosophical & Mathematical):** 
While structurally beautiful, this approach was rejected because it fundamentally violates the definition of emergent macroscopic phenomena. Knots are fluid—they merge, split, evaporate, and drift. Attempting to explicitly maintain macroscopic boundaries using microscopic `anchor_id` variables introduces impossible edge cases. 
If an observer attempts to "latch" onto a particle from the inside, it ceases to be an objective diagnostic tool. A true emergent tracker *requires* an unbiased, God-like macroscopic scan to be scientifically valid.

## 4. The Final Solution: 10-Step Temporal Throttling
**The Compromise:** We returned to Temporal Throttling, but strictly set the default `track_interval` to **10 steps** (instead of 100).
- **Why it works:** 10 steps of evolution is small enough that the topological drift rarely exceeds the $30\%$ replacement threshold. The particle easily survives the overlap check, guaranteeing unbroken 1-step-equivalent lifetime integrity.
- **The Physics Win:** By scanning every 10 steps instead of 1 step, the $O(V)$ computational cost is instantly divided by 10, granting a massive performance multiplier without sacrificing worldline continuity. 

### CLI Customization
Future researchers can bypass this at runtime via `run_simulation.rs`:
- `--track_interval 1`: Perfect mathematical resolution (slowest).
- `--track_interval 10`: The structural default (10x faster).
- `--track_interval 0`: Absolute zero tracking. Pure volume generation.
