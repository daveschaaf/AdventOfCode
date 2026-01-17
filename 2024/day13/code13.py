from sympy import Integer
from sympy.matrices import Matrix

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
    def __init__(self, machine_data, part = 1):
        a_x, a_y = (Integer(n) for n in machine_data["A"])
        b_x, b_y = (Integer(n) for n in machine_data["B"])
        # Standard numpy matrices
        self.matrix = Matrix([[a_x, b_x],
                              [a_y, b_y]])
        self.prize = Matrix([Integer(n) for n in machine_data['prize']])
        if part != 1:
            correction = Integer(10_000_000_000_000)
            self.prize += Matrix([correction, correction])
        self.token_cost = Matrix([3, 1])
    
    def solve(self):
        solution = self.matrix.LUsolve(self.prize)
        if all(x.q == 1 for x in solution):
            return solution.dot(self.token_cost)
        return 0

def calc_tokens(part):
    with open('data13.dat', 'r') as file:
        file_content = file.read()
    data = parse_data(file_content)
    tokens = 0
    for machine in data:
        tokens += ClawMachine(machine, part).solve()
    return tokens

def part1():
    return calc_tokens(1)

def part2():
    return calc_tokens(2)
