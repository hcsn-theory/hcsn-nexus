# HCSN: Higher-Order Causal Structure Networks

### *Simulating Emergent Topological Matter*

---

## 🌌 Project Overview

**HCSN** is a computational framework designed to validate the theory of matter emergence within topological rewrite systems. Rather than utilizing ad-hoc particle injection, HCSN models a purely structural universe where "Topological Knots"—persistent, localized structural motifs—emerge spontaneously from background vacuum dynamics.

This workspace (Nexus) contains the formal theory, the high-performance core engine, the visualization pipeline, and telemetry observability.

---

## 📂 Repository Structure (The Nexus)

| Repository | Description | Status |
|------------|-------------|--------|
| **[hcsn-theory](hcsn-theory/)** | Formal Scientific Papers and Canon (Docs 01–05). | ✅ Stable |
| **[hcsn-rust](hcsn-rust/)** | Core High-Performance Simulation Engine. | ✅ Phase 12 |
| **[hcsn-viz](hcsn-viz/)** | **Visualization Layer** (The Obsidian Observer). | ✅ Active |
| **[hcsn-website](hcsn-website/)** | Research Hub Landing Page & Docs Browser. | ✅ Production |
| **[hcsn-gantry](hcsn-gantry/)** | Observability, Telemetry & Multi-Worker Pipeline. | ✅ Active |
| **[hcsn-sim](hcsn-sim/)** | Legacy Python Implementation (Backport only). | ⚠️ Legacy |

---

## 📡 The Obsidian Observer: HCSN Visualization

> [!IMPORTANT]
> **Engine Physics vs. Visual Artifice**
> The `hcsn-rust` engine operates purely on topological graph transformations. To facilitate human observation, the **[hcsn-viz](hcsn-viz/)** layer introduces several **Artificial Visual Constructs** that do not exist in the engine's physical laws:
>
> 1. **3D Spatial Embedding**: The engine is purely structural; the visualizer chooses 3D coordinates based on a custom layout algorithm.
> 2. **Macro-Physics (Centroids, Repulsion)**: To prevent visual clutter and overlapping matter, the visualizer implements a 3D repulsion/attraction system for "Knots." This is an *observational aid* only.
> 3. **Volumetric Rendering**: The glows, nebulae, and lighting effects are GPU-accelerated cinematic layers used to highlight regions of high structural coherence.
>
> **Unidirectional Data Flow**: These visual dynamics are non-reciprocal. The visualizer *observes* the engine, but visual artifacts (like node repulsion or bloom) provide **zero feedback** to the hcsn-rust engine. No conclusions derived from visual layout are imported back into the engine's physics.

---

## 🚀 Getting Started

1. **Engine**: Navigate to `hcsn-rust/` and run `cargo run --release`.
2. **Visualizer**: Open `hcsn-viz/index.html` in a modern browser (RTX recommended).
3. **Telemetry**: Monitor runs via `hcsn-gantry/` observer dashboard.
4. **Data Stream**: The engine broadcasts state via the Obsidian WebSocket protocol (default `ws://localhost:8765`).

---

## 📜 License

This entire Nexus workspace is distributed under the **MIT License**. See `LICENSE` for details.
