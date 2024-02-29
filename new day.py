from qiskit import QuantumCircuit, transpile
from qiskit_aer.aerprovider import AerProvider as Aer


def random_number():
    # Create a quantum circuit with one qubit
    qc = QuantumCircuit(4)

    # Apply a Hadamard gate to put the qubit in a superposition state
    qc.h(3)
    qc.h(2)
    qc.h(1)
    qc.h(0)
    # Measure the qubit
    qc.measure_all()

    # Use the Aer simulator to run the circuit
    simulator = Aer().get_backend('qasm_simulator')
    job = simulator.run(transpile(qc, simulator))
    result = job.result()

    # Get the measurement counts
    counts = result.get_counts(qc)

    # Convert the counts to a list of measurement outcomes
    outcome = list(counts.keys())[0]

    # Convert the binary outcome to an integer
    random_number = int(outcome, 2)
    return random_number

for i in range(10):
    print("Random number:", random_number())