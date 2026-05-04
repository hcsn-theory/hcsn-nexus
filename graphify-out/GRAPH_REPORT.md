# Graph Report - hcsn-nexus  (2026-05-04)

## Corpus Check
- 223 files · ~175,934 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 708 nodes · 789 edges · 61 communities detected
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 46 edges (avg confidence: 0.77)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b781bf4b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 118|Community 118]]

## God Nodes (most connected - your core abstractions)
1. `main()` - 31 edges
2. `RewriteEngine` - 24 edges
3. `RewriteEngine` - 23 edges
4. `Hypergraph` - 19 edges
5. `Hypergraph` - 14 edges
6. `cn()` - 12 edges
7. `TelemetryClient` - 8 edges
8. `compute_omega()` - 7 edges
9. `ForceLayout3D` - 7 edges
10. `hierarchical_closure()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `run_simulation_loop()` --calls--> `compute_omega()`  [INFERRED]
  hcsn-viz/src/main.rs → hcsn-rust/src/observables.rs
- `main()` --calls--> `handle_client()`  [EXTRACTED]
  hcsn-gantry/gantry-supervisor/src/main.rs → hcsn-viz/src/main.rs
- `main()` --calls--> `init_pool()`  [INFERRED]
  hcsn-gantry/gantry-supervisor/src/main.rs → hcsn-gantry/observer-server/src/db.rs
- `RewriteEngine` --uses--> `TopologicalKnot`  [INFERRED]
  hcsn-sim/engine/rewrite_engine.py → hcsn-sim/engine/observables.py
- `main()` --calls--> `run_simulation_loop()`  [EXTRACTED]
  hcsn-gantry/gantry-supervisor/src/main.rs → hcsn-viz/src/main.rs

## Communities (183 total, 30 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.09
Nodes (27): get_mem_usage_percent(), main(), emit_export_telemetry(), ensure_binaries_built(), env_bool(), env_f64(), env_u16(), env_u32() (+19 more)

### Community 1 - "Community 1"
Cohesion: 0.07
Nodes (24): ChiBin, dot(), ForceLawStats, mag(), main(), ScatteringDist, SymmetryProfile, main() (+16 more)

### Community 2 - "Community 2"
Cohesion: 0.08
Nodes (22): main(), average_large_interval(), causal_interval_size(), closure_density(), coarse_grain_interactions(), compute_coherence_raw(), count_triangles(), defect_density() (+14 more)

### Community 3 - "Community 3"
Cohesion: 0.09
Nodes (28): HealthPoint, init_pool(), insert_batch(), insert_raw(), latest_logs(), latest_panic(), metric_points(), recent_events() (+20 more)

### Community 4 - "Community 4"
Cohesion: 0.09
Nodes (10): Hyperedge, Hypergraph, Maximum causal chain length in the hypergraph., k-ary relation between vertices., Core data structure for HCSN.     Represents a causal quantum hypergraph., Add causal relation u → v and update worldline depth., Degree: number of hyperedges containing v., Vertex (+2 more)

### Community 5 - "Community 5"
Cohesion: 0.08
Nodes (8): RootLayout(), Badge(), Card(), Header(), MetricsPanel(), ThemeProvider(), useObserver(), cn()

### Community 6 - "Community 6"
Cohesion: 0.17
Nodes (5): ConservationMode, DefectLogEntry, EmergenceMode, RewriteEngine, XiCurrentLogEntry

### Community 7 - "Community 7"
Cohesion: 0.12
Nodes (3): Hyperedge, Hypergraph, Vertex

### Community 9 - "Community 9"
Cohesion: 0.16
Nodes (11): defect_acceleration(), defect_momentum(), defect_momentum_at_time(), momentum_timeseries(), Discrete acceleration from momentum series., Momentum measured at an arbitrary observation time., Returns (times, momenta) for one defect., Purely observational momentum:     imbalance of defect events around this defect (+3 more)

### Community 10 - "Community 10"
Cohesion: 0.38
Nodes (10): bytes_to_hex(), decode_envelopes(), decode_logs(), decode_metrics(), decode_traces(), find_attr(), nanos_to_ts(), number_point_value() (+2 more)

### Community 12 - "Community 12"
Cohesion: 0.25
Nodes (6): DocsSidebar(), DocsLayout(), DocsIndex(), getAllDocs(), getDocBySlug(), generateStaticParams()

### Community 14 - "Community 14"
Cohesion: 0.22
Nodes (8): IngestBatch, LogEvent, MetricEvent, PanicEvent, TelemetryEnvelope, TelemetryKind, TelemetryPayload, TraceEvent

### Community 15 - "Community 15"
Cohesion: 0.39
Nodes (5): compute_correlation(), compute_mle_alpha(), main(), TrackerConfig, TrackerState

### Community 16 - "Community 16"
Cohesion: 0.6
Nodes (5): analyze_all_seeds(), extract_kinematics(), piecewise_linear(), power_law(), sigmoid()

### Community 17 - "Community 17"
Cohesion: 0.47
Nodes (5): analyze_phase_space(), causal_hierarchy_report(), main(), Tests: Does Age -> Stability? Or Independent?, Main Research Logic: Maps R2 and Signal Gain across (Age, Stability) space.

### Community 18 - "Community 18"
Cohesion: 0.47
Nodes (5): build_interaction_graph(), extract_worldlines(), main(), Build a graph where nodes are worldlines     and edges indicate shared hyperedge, Identify worldline vertices by depth threshold.

### Community 19 - "Community 19"
Cohesion: 0.5
Nodes (4): Event, fit_branching_ratio(), FitResult, main()

### Community 20 - "Community 20"
Cohesion: 0.6
Nodes (4): extract_force_series(), main(), Reconstruct instantaneous force proxy     using rewrite-flux imbalance between c, sliding_window_force()

### Community 21 - "Community 21"
Cohesion: 0.9
Nodes (4): covariance(), main(), mean(), std()

### Community 22 - "Community 22"
Cohesion: 0.8
Nodes (4): covariance(), main(), mean(), std()

### Community 24 - "Community 24"
Cohesion: 0.67
Nodes (3): calculate_alpha(), main(), PureStats

### Community 25 - "Community 25"
Cohesion: 0.83
Nodes (3): compute_2d_conditional_variance(), compute_conditional_variance(), main()

### Community 26 - "Community 26"
Cohesion: 0.83
Nodes (3): clear_scene(), load_frames(), run_import()

### Community 27 - "Community 27"
Cohesion: 0.67
Nodes (3): main(), Run a single universe for given p_create., run_experiment()

### Community 28 - "Community 28"
Cohesion: 0.67
Nodes (3): detect_clusters(), main(), Detect and track proto-particles (ξ-clusters) by cluster ID.      Returns:

### Community 29 - "Community 29"
Cohesion: 0.83
Nodes (3): defect_support(), main(), persistence()

### Community 30 - "Community 30"
Cohesion: 0.83
Nodes (3): defect_support(), main(), persistence()

### Community 31 - "Community 31"
Cohesion: 0.83
Nodes (3): bfs_cluster_distance(), is_finite(), main()

### Community 32 - "Community 32"
Cohesion: 1.0
Nodes (3): main(), mean(), variance()

### Community 33 - "Community 33"
Cohesion: 0.83
Nodes (3): defect_support(), influenced(), main()

### Community 34 - "Community 34"
Cohesion: 0.83
Nodes (3): defect_support(), main(), persistence()

## Knowledge Gaps
- **57 isolated node(s):** `UndoRecord`, `TopologicalKnot`, `InteractionEvent`, `DefectLogEntry`, `XiCurrentLogEntry` (+52 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **30 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `main()` connect `Community 0` to `Community 3`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Why does `compute_omega()` connect `Community 1` to `Community 0`, `Community 6`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Why does `run_simulation_loop()` connect `Community 0` to `Community 1`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `main()` (e.g. with `.generate_filename()` and `.open_writer()`) actually correct?**
  _`main()` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `RewriteEngine` (e.g. with `ForceLayout3D` and `TopologicalKnot`) actually correct?**
  _`RewriteEngine` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `UndoRecord`, `TopologicalKnot`, `InteractionEvent` to the rest of the system?**
  _57 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.09 - nodes in this community are weakly interconnected._