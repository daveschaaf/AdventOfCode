def parse_data(raw_data):
    machine_data = raw_data.split("\n\n")
    parsed_data = []
    for machine in machine_data:
        elements = machine.split("\n")
        a_button = elements[0].split("A: ")[1].split(", ")
        b_button = elements[1].split("B: ")[1].split(", ")
        prize = elements[2].split(": ")[1].split(", ")
        parsed_machine = {}
        parsed_machine["A"] = [ int(move.split("+")[1]) for move in a_button]
        parsed_machine["B"] = [ int(move.split("+")[1]) for move in b_button]
        parsed_machine["prize"] = [ int(move.split("=")[1]) for move in prize]
        parsed_data.append(parsed_machine)
    return parsed_data

class ClawMachine():
    def __init__(self, machine_data):
       self.machine_data = machine_data

