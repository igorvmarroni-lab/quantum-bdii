from qiskit import QuantumCircuit
import numpy as np

def create_bdii_circuit(hr: float = 0.568, n_qubits: int = 4) -> QuantumCircuit:
    qc = QuantumCircuit(n_qubits, n_qubits)

    theta = 2 * np.arcsin(np.sqrt(hr))

    qc.h(range(n_qubits))

    for i in range(n_qubits):
        qc.ry(theta * (i + 1) / n_qubits, i)

    for i in range(n_qubits - 1):
        qc.cx(i, i + 1)

    qc.h(0)
    qc.cx(0, n_qubits - 1)

    qc.measure(range(n_qubits), range(n_qubits))

    return qc
