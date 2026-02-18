from qiskit_aer import AerSimulator
from qiskit import transpile
# Import your circuit function
from .circuit import create_bdii_circuit  # ajuste se necessário

qc = create_bdii_circuit()
sim = AerSimulator()
qc_t = transpile(qc, sim)
result = sim.run(qc_t, shots=5000).result()
print("Aer simulation completed - HR should match hardware 0.568")
