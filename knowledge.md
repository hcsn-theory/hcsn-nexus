# Comprehensive HCSN Theory Knowledge Base

**Hierarchical Causal Structure Networks (HCSN)** is a causal theory of everything that aims to derive physics entirely from a discrete, computational substrate, refusing to assume spacetime, manifolds, wavefunctions, or background clocks.

This document serves as the complete theoretical extraction from the canonical documents of the `test-hcsn-theory` repository.

---

## 1. Axioms and Methodology

### The Minimal Substrate
At the most fundamental level, the universe is modeled as a finite but unbounded **hypergraph**:
- **Vertices**: Discrete events.
- **Hyperedges**: Directed causal relations.
- **Partial Ordering ($\preceq$)**: Strict causal consistency is enforced (Irreflexivity and Transitivity), forming a Directed Acyclic Graph (DAG) and explicitly forbidding closed causal loops.

### Evolution via Rewrites
The network evolves via strictly local rewrite rules applied to finite subgraphs. These rewrites respect causal order, update the topology, and irreversibly transform the structure. 
- **Time** is simply the "rewrite depth" (the count of irreversible rewrites). 
- There is no background clock. Time emerges from the sequential causality of rewrites.

### The Regulatory Tension
Dynamics are governed by a tension to maintain **Hierarchical Closure ($\Omega$)**. $\Omega$ serves as an order parameter describing multi-scale causal consistency. The theory permits localized violations of this regulatory balance, known as **Defects**.

---

## 2. Defects, Worldlines, and Emerging Particles

Since there is no "space" to contain particles, objects must emerge structurally.

### Defects
A defect is a localized event where the hierarchical closure $\Omega$ undergoes a discontinuous change ($|\Delta\Omega| > \epsilon$). 
- **Defect Charge ($Q$)**: Defined as $\Delta\Omega$.
- Defects act as regulated instabilities that suppress further structural fluctuation.

### Worldlines and Proto-Objects
Defects that persist over multiple rewrite steps form **worldlines**. 
- Identity is not based on remaining the same "stuff" (vertices turn over completely), but on **overlap continuity**: $ \frac{|C(t) \cap C(t+1)|}{|C(t) \cup C(t+1)|} \ge \alpha $.
- A persistent cluster of the transport field $\xi$ ($\xi > 0$) is a **proto-object**.

### Defining a "Particle"
A proto-object formally behaves as a particle if it meets four empirical criteria:
1. **Persistence**: Its lifetime $\tau \gg \tau_{correlation}$.
2. **Momentum Coherence**: It has bounded rewrite variance.
3. **Inertial Stability**: Mass scales inversely with momentum variance.
4. **Structural Coupling**: Stability correlates with $\Omega$.

---

## 3. Kinematics, Dynamics, and Mass

### Relational Motion
There are no trajectories in a manifold. Dynamics is strictly defined as "persistence and transformation under rewrite flow". 

### Mass and Momentum
In standard physics, mass creates inertia. In HCSN, inertia defines mass.
- **Rewrite Imbalance**: A worldline shows "momentum" if rewrites happen preferentially on one side of its causal support more than the other. Momentum is the statistical persistence of this imbalance.
- **Mass ($m$)**: Defined empirically as the inverse variance of momentum ($m \sim \frac{1}{\text{Var}(p)}$). Long-lived worldlines have low momentum variance, defining a high emergent mass.

### Interaction via Competition
Proto-particles do not interact by exchanging force carriers in a background space. Instead, they interact via **Rewrite Competition**.
- Causal clusters compete for access to the $\Omega$-modulated rewrite pool.
- Interaction strength is proportional to the **Rewrite Flux Imbalance**: $F_{AB} = \frac{|\Phi_A - \Phi_B|}{\tau_{coexist}}$.
- This interaction is inherently **asymmetric**, **non-conservative**, and **environment-mediated**.

---

## 4. Geometry and Phase Transitions

Geometry is the macroscopic limit of causal regularity. However, not all causal graphs produce a stable space.

### Phase Regimes
The hierarchical closure $\Omega$ dictates distinct phases of the universe:
1. **Subcritical ($\Omega < 1.0$)**: Defects are transient ($\tau < 100$ steps) and highly unstable. No information transport occurs.
2. **Critical ($\Omega \approx 1.1$)**: Marginal stability. A phase transition point.
3. **Supercritical ($\Omega > 1.2$)**: Defect worldlines are incredibly persistent ($\tau > 10^4$). The transport field $\xi$ propagates stably without unbounded spreading.

### Dimension vs. Coordination
An important correction in HCSN theory: the average coordination number $\langle k \rangle$ is not the true dimension. 
Dimension is an effective scaling parameter ($D_{\text{eff}}(r) = \frac{d \log N(r)}{d \log r}$), dependent on coarse-graining. While theoretical simulations show $D_{\text{eff}}$ stabilizing in the supercritical phase (approx. range 3–5), the exact analytical mechanism for dimensional selection remains an **open problem**.

---

## 5. Falsifiability and Limits

HCSN is a rigorous, falsifiable framework. It does *not* claim to have fully derived the Standard Model or exact General Relativity symmetry groups yet. 
If simulations demonstrate that stable particles or Lorentz attractors cannot form without breaking fundamental causality, the theory considers itself invalidated. Currently, HCSN has successfully demonstrated emergent finite signal speeds, strictly consistent causality, and the formation of persistent, mass-bearing defect structures.
