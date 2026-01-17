import numpy as np
import numpy.testing as npt
from code13 import parse_data, ClawMachine, part1

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
    assert machine_data["prize"] == (8400, 5400)

def test_claw_machine():
    data = parse_data(sample)
    claw = ClawMachine(data[0])
    npt.assert_allclose(claw.prize, np.array((8400, 5400)))
    assert claw.a_increase_x == 94
    assert claw.a_increase_y == 34
    assert claw.b_increase_x == 22
    assert claw.b_increase_y == 67

def test_claw_solution():
    data = parse_data(sample)
    claw1 = ClawMachine(data[0])
    claw2 = ClawMachine(data[1])
    claw3 = ClawMachine(data[2])
    claw4 = ClawMachine(data[3])

    npt.assert_allclose(claw1.solution(claw1.prize), np.array([80, 40]))
    npt.assert_allclose(claw2.solution(claw2.prize), np.array([0, 0]))
    npt.assert_allclose(claw3.solution(claw3.prize), np.array([38, 86]))
    npt.assert_allclose(claw4.solution(claw4.prize), np.array([0, 0]))

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
    claw4 = ClawMachine(data[3])
    npt.assert_allclose(claw4.converted_prize, claw4.prize + 10000000000000)

def test_big_solve():
    data = parse_data(sample)
    claw1 = ClawMachine(data[0])
    claw2 = ClawMachine(data[1])
    claw3 = ClawMachine(data[2])
    claw4 = ClawMachine(data[3])
    
    assert claw1.big_solve() == 0
    assert claw2.big_solve() > 0
    assert claw3.big_solve() == 0
    assert claw4.big_solve() > 0
