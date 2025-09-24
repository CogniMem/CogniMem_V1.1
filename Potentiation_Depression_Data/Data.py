## Modeling STDP from Memristive Device Measurements

To incorporate biologically inspired plasticity into spiking neural networks, we derive an empirical spike-timing dependent plasticity (STDP) function from conductance measurements of memristive synaptic devices. The dataset comprises two continuous sequences of conductance values: one corresponding to long-term potentiation (LTP), denoted as $G_{\text{pot}}$, and the other to long-term depression (LTD), denoted as $G_{\text{dep}}$.

From each sequence, we compute the relative change in conductance using the normalized difference formula:

$$
\frac{\Delta G}{G_0} = \frac{G_{t+1} - G_t}{G_t + \varepsilon}
$$

where $\varepsilon$ is a small constant to ensure numerical stability. This yields two sequences of fractional conductance changes: one for potentiation and one for depression.

Each relative change is then mapped to a biologically meaningful spike timing difference $\Delta t$. Potentiation changes are associated with positive $\Delta t$ values, representing causal spike pairings ($\text{pre} \rightarrow \text{post}$), while depression changes are associated with negative $\Delta t$ values, reflecting anti-causal pairings ($\text{post} \rightarrow \text{pre}$). Specifically, we set:

$$
\Delta t_{\text{pot}} \in [1, 5] \quad \text{and} \quad \Delta t_{\text{dep}} \in [-5, -1]
$$

using uniformly sampled values to mimic experimental timing conditions.
