import numpy as np
from decimal import Decimal
from sympy import N, Integer
from sympy.matrices.exceptions import NonInvertibleMatrixError
from sympy import init_printing
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
        parsed_machine["A"] = tuple([ int(move.split("+")[1]) for move in a_button])
        parsed_machine["B"] = tuple([ int(move.split("+")[1]) for move in b_button])
        parsed_machine["prize"] = tuple([ int(move.split("=")[1]) for move in prize])
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
            self.prize += Matrix([Integer(10000000000000), Integer(10000000000000)])
        self.token_cost = Matrix([3, 1])
    
    def solve(self):
        def is_sp_int(x, tol=1e-16):
            if x.is_Integer:
                return True
            if x.is_Rational:
                return x.q == 1
            return abs(x % 1) < tol
        try:
            solution = self.matrix.LUsolve(self.prize)
        except NonInvertibleMatrixError:
            return 0
        dot_product = solution.dot(self.token_cost)
        if all(is_sp_int(x) for x in solution) and is_sp_int(dot_product):
            return Integer(dot_product)
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
