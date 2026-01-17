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
        parsed_machine["A"] = [ int(move.split("+")[1]) for move in a_button]
        parsed_machine["B"] = [ int(move.split("+")[1]) for move in b_button]
        parsed_machine["prize"] = tuple([ int(move.split("=")[1]) for move in prize])
        parsed_data.append(parsed_machine)
    return parsed_data

class ClawMachine():
    def __init__(self, machine_data):
        self.a_increase_x = machine_data["A"][0]
        self.a_increase_y = machine_data["A"][1]
        self.b_increase_x = machine_data["B"][0]
        self.b_increase_y = machine_data["B"][1]
        # Standard numpy matrices
        self.matrix = np.array([[self.a_increase_x, self.b_increase_x],
                                [self.a_increase_y, self.b_increase_y]])
        self.prize = np.array(machine_data['prize'])
        # convert to Symbolic python for large digits
        self.sp_matrix = Matrix(self.matrix)
        self.converted_prize = Matrix(self.prize + Integer(10000000000000))

    def solution(self):
        solution = np.linalg.solve(self.matrix, self.prize)
        if np.all(np.isclose(solution, np.round(solution), atol=1e-15)):
            return solution
        return np.array([0, 0])

    def solve(self):
        return np.dot(self.solution(), np.array([3, 1]))

    def big_solve(self):
        def is_sp_int(x, tol=1e-16):
            if x.is_Integer:
                return True
            if x.is_Rational:
                return x.q == 1
            return abs(x % 1) < tol
        try:
            solution = self.sp_matrix.LUsolve(self.converted_prize)
        except NonInvertibleMatrixError:
            return 0
        dot_product = solution.dot(Matrix([3, 1]))
        if all(is_sp_int(x) for x in solution) and is_sp_int(dot_product):
            return Integer(dot_product)
        return 0

def part1():
    with open('data13.dat', 'r') as file:
        file_content = file.read()
    data = parse_data(file_content)
    tokens = 0
    for machine in data:
        tokens += ClawMachine(machine).solve()
    return tokens

def part2():
    with open('data13.dat', 'r') as file:
        file_content = file.read()
    data = parse_data(file_content)
    tokens = 0
    for machine in data:
        tokens += ClawMachine(machine).big_solve()
    return tokens

