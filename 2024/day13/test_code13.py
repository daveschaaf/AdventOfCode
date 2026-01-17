import pytest
from sympy import Integer
from sympy.matrices import Matrix
from code13 import parse_data, ClawMachine, part1, part2

sample = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

def test_parse_data():
    data = parse_data(sample)
    machine_data = data[0]
    assert machine_data["A"] == [94, 34]
    assert machine_data["B"] == [22, 67]
    assert machine_data["prize"] == [8400, 5400]

def test_claw_machine():
    data = parse_data(sample)
    claw = ClawMachine(data[0])
    assert claw.prize[0] == Integer(8400)
    assert claw.prize[1] == Integer(5400)
    assert claw.matrix == Matrix([[94, 22],
                                  [34, 67]])
    assert claw.token_cost == Matrix([3, 1])

def test_claw_solve():
    data = parse_data(sample)
    claw1 = ClawMachine(data[0])
    claw2 = ClawMachine(data[1])
    claw3 = ClawMachine(data[2])
    claw4 = ClawMachine(data[3])
    assert claw1.solve() == 280
    assert claw2.solve() == 0
    assert claw3.solve() == 200
    assert claw4.solve() == 0

def test_part_1():
    assert part1() == 35255
    # 26767 too low


def test_converted_prize():
    data = parse_data(sample)
    claw1 = ClawMachine(data[0], 2)
    assert claw1.prize[0] == Integer(10000000008400)
    assert claw1.prize[1] == Integer(10000000005400)

def test_big_solve():
    data = parse_data(sample)
    claw1 = ClawMachine(data[0], 2)
    claw2 = ClawMachine(data[1], 2)
    claw3 = ClawMachine(data[2], 2)
    claw4 = ClawMachine(data[3], 2)
    
    assert claw1.solve() == 0
    assert claw2.solve() > 0
    assert claw3.solve() == 0
    assert claw4.solve() > 0

def test_part_2():
    assert part2() == Integer(87582154060429)
    # 60522696580589 too low
