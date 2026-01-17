import numpy as np
from decimal import Decimal
import sympy as sp

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
        self.a_cost = 3
        self.b_cost = 1
        self.matrix = np.array([[self.a_increase_x, self.b_increase_x],
                                [self.a_increase_y, self.b_increase_y]])
        self.prize = np.array(machine_data['prize'])
        self.converted_prize = np.array([self.prize + Decimal(10000000000000)], dtype=object)

    def solution(self, prize):
        solution = np.linalg.solve(self.matrix, prize)
        if np.all(np.isclose(solution, np.round(solution), atol=1e-15)):
            return solution
        return np.array([0, 0])

    def sympy_solution(self):
        pass
        # TODO implement self.solution with sympy

    def solve(self):
        return np.dot(self.solution(self.prize), np.array([3, 1]))

    def big_solve(self):
        solution = self.solution(self.converted_prize)
        print(f"{solution=}")
        print(f"{np.dot(solution, np.array([3, 1]))}")
        return np.dot(solution, np.array([3, 1]))


def part1():
    with open('data13.dat', 'r') as file:
        file_content = file.read()
    data = parse_data(file_content)
    tokens = 0
    for machine in data:
        tokens += ClawMachine(machine).solve()
    return tokens

