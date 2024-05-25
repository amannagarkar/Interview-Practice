class Gate:
    def __init__(self, flight_name):
        self.gates = {}

    def gate_exists(self, gate_id):
        return gate_id in self.gates

    def add_gate(self, gate_id):
        if gate_id not in self.gates:
            self.gates[gate_id] = 0
        else:
            print("Gate already exists")

    def add_flight_to_gate(self, flight_id, gate_id):
        if gate_id not in self.gates:
            return "Invalid gate id"

        self.gates[gate_id] = flight_id
        return f"{flight_id} departs from gate {gate_id}"

    def schedule_flight(self, gate_id, flight_id):
        return

    def depart_flight(self, gate_id):
        if self.gate_exists and self.gates[gate_id]:
            return f"{self.gates[gate_id]} departed"

        return f"No flight at gate {gate_id}"
