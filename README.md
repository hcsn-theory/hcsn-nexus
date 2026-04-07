# HCSN: Higher-Order Causal Structure Networks

### *Simulating Emergent Topological Matter*

---

## 🌌 Project Overview

**HCSN** is a computational framework designed to validate the theory of matter emergence within topological rewrite systems. Rather than utilizing ad-hoc particle injection, HCSN models a purely structural universe where "Topological Knots"—persistent, localized structural motifs—emerge spontaneously from background vacuum dynamics.

This repository contains the core high-performance Rust engine, the theory documentation, and a high-fidelity cinematic observer (Visualizer).

---

## 📂 Repository Structure

- **`hcsn-rust/`**: The core simulation engine. High-performance topological rewrite logic.
- **`visualization/`**: The "Obsidian Observer." A GPU-accelerated 3D environment for real-time monitoring of matter emergence.
- **`hcsn-theory/`**: Formal documentation and scientific underpinnings of the structural matter condensation theory.

---

## 📡 The Obsidian Observer: A Crucial Distinction

> [!IMPORTANT]
> **Engine Physics vs. Visual Artifice**
> The `hcsn-rust` engine operates purely on topological graph transformations. To facilitate human observation, the `visualization` layer introduces several **Artificial Visual Constructs** that do not exist in the engine's physical laws:
>
> 1. **3D Spatial Embedding**: The engine is purely structural; the visualizer chooses 3D coordinates based on a custom layout algorithm.
> 2. **Macro-Physics (Centroids, Repulsion)**: To prevent visual clutter and overlapping matter, the visualizer implements a 3D repulsion/attraction system for "Knots." This is an *observational aid* only.
> 3. **Volumetric Rendering**: The glows, nebulae, and lighting effects are GPU-accelerated cinematic layers used to highlight regions of high structural coherence.
>
> **Unidirectional Data Flow**: These visual dynamics are non-reciprocal. The visualizer *observes* the engine, but visual artifacts (like node repulsion or bloom) provide **zero feedback** to the hcsn-rust engine. No conclusions derived from visual layout are imported back into the engine's physics.

---

## 🚀 Getting Started

1. **Engine**: Navigate to `/hcsn-rust` and run `cargo run --release`.
2. **Visualizer**: Open `/visualization/index.html` in a modern browser (RTX recommended).
3. **Data Stream**: The engine broadcasts state via the Obsidian WebSocket protocol (default `ws://localhost:8765`).

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for details.
