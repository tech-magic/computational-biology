import numpy as np
from scipy.optimize import minimize

from qiskit import QuantumCircuit, transpile
from qiskit.circuit import ParameterVector
from qiskit_aer import AerSimulator

# -------------------------------
# Simulator Backend (like simulating inside brain's container of all neurons)
# -------------------------------
backend = AerSimulator()

# -------------------------------
# Input signals - Analog values (e.g., dendritic inputs)
# Superposition simulates analog variability
# -------------------------------
input_signals = np.array([np.pi/3, np.pi/4])  # signal strengths for dendrites

# -------------------------------
# Synaptic weights - trainable quantum parameters
# Learning through parameter optimization (simulating synaptic plasticity)
# -------------------------------
theta = ParameterVector('θ', 2)

def construct_circuit(inputs, parameters):
    """Quantum circuit simulating a biological neuron"""
    qc = QuantumCircuit(2)

    # -------------------------------
    # Superposition simulates analog variability
    # Hadamard gate allows qubits to exist in mixed states (not binary)
    # -------------------------------
    qc.h(0)
    qc.h(1)

    # -------------------------------
    # Dynamic input encoding using Ry rotations
    # Simulates dendritic input of varying strength and timing
    # -------------------------------
    qc.ry(inputs[0], 0)
    qc.ry(inputs[1], 1)

    # -------------------------------
    # Entanglement enables rich signal integration
    # Like how dendrites' effects combine non-linearly
    # -------------------------------
    qc.cx(0, 1)

    # -------------------------------
    # Rotation angles on Bloch sphere as trainable synaptic weights
    # Encodes continuous-valued influence on neuron firing
    # -------------------------------
    qc.ry(parameters[0], 0)
    qc.ry(parameters[1], 1)

    # -------------------------------
    # Asynchronous, parallel processing
    # Quantum circuits have no global clock — fire when locally ready
    # Distributed architecture — like biological neurons
    # -------------------------------

    # -------------------------------
    # Probabilistic output via quantum measurement
    # Collapses into firing state (like axon firing)
    # -------------------------------
    qc.measure_all()

    return qc

def evaluate_cost(params):
    """Cost function that encourages the neuron to 'fire' (not remain in |00⟩)"""
    qc = construct_circuit(input_signals, params)

    compiled = transpile(qc, backend)
    job = backend.run(compiled, shots=1024)
    result = job.result()
    counts = result.get_counts()

    # -------------------------------
    # Probabilistic axon firing outcome — like stochastic synaptic release
    # Here we define '00' as no firing, so minimize it
    # -------------------------------
    prob_00 = counts.get('00', 0) / 1024
    cost = prob_00
    print(f"Params: {params}, Cost: {cost:.4f}")
    return cost

# -------------------------------
# Initial random synaptic weights (θ)
# -------------------------------
initial_theta = np.random.uniform(0, 2 * np.pi, 2)

# -------------------------------
# Learning through classical optimization — Hebbian-style update
# -------------------------------
opt_result = minimize(evaluate_cost, initial_theta, method='COBYLA')

# -------------------------------
# Final trained weights after learning
# -------------------------------
trained_theta = opt_result.x
print("\nFinal trained parameters (synaptic weights):", trained_theta)

# -------------------------------
# Final quantum neuron circuit showing trained behavior
# -------------------------------
final_qc = construct_circuit(input_signals, trained_theta)
print("\nTrained quantum neuron circuit:")
print(final_qc.draw())
