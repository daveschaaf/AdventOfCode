# Test 2024 Day 7
import pytest
from code07 import * 

sample = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

sample_data = parse_sample(sample)

with open('07_data.dat', 'r') as file:
    data = parse_part_1(file)
def test_parse_sample():
    assert sample_data[0] == [190, [10, 19]], 'parses the first sample line'
    assert sample_data[1] == [3267, [81, 40, 27]], 'parses the second sample line'
    assert len(sample_data) == 9, 'parses all the lines'

def test_parse_part_1():
    assert data[0] == [21006540, [25, 34, 307, 82, 27
]], 'parses the first line'
    assert data[1] == [3040, [579, 5, 7, 113, 25, 1]], 'parses the second line'
    assert len(data) == 850, 'parses all the lines'
def test_calculator_class():
    
    calculator = Calculator(35, [5, 7])
    node = calculator.nodes[0]
    assert node.plus_val == 12
    assert node.multiply_val == 35
    assert calculator.calculate() == True

    
    calculator = Calculator(35, [5, 5])
    node = calculator.nodes[0]
    assert node.plus_val == 10
    assert node.multiply_val == 25
    assert calculator.calculate() == False

def test_calculate_calibration():
    assert calculate_calibration(sample_data) == 3749
    assert calculate_calibration(data) == 3598800864292

