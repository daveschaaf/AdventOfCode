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
    data = parse_data(file)
def test_parse_sample():
    assert sample_data[0] == [190, [10, 19]], 'parses the first sample line'
    assert sample_data[1] == [3267, [81, 40, 27]], 'parses the second sample line'
    assert len(sample_data) == 9, 'parses all the lines'

def test_parse_data():
    assert data[0] == [21006540, [25, 34, 307, 82, 27
]], 'parses the first line'
    assert data[1] == [3040, [579, 5, 7, 113, 25, 1]], 'parses the second line'
    assert len(data) == 850, 'parses all the lines'
def test_calculator_class():
    
    calculator = Calculator(35, [5, 7])
    node = calculator.nodes[0]
    assert node.plus_val == 12
    assert node.multiply_val == 35
    assert node.concat_val == 57
    assert calculator.calc_part_1() == True

    
    calculator = Calculator(35, [5, 5])
    node = calculator.nodes[0]
    assert node.plus_val == 10
    assert node.multiply_val == 25
    assert node.concat_val == 55
    assert calculator.calc_part_1() == False


def test_calculate_calibration():
    assert calculate_calibration(sample_data) == 3749
    assert calculate_calibration(data) == 3598800864292

def test_concat():

    def assert_node(node, val_1, val_2):
        assert node.val_1 == val_1
        assert node.val_2 == val_2
        assert node.concat_val == int(str(val_1)+str(val_2))
        assert node.multiply_val == val_1 * val_2
        assert node.plus_val == val_1 + val_2


    node = Calculator.CalcNode(48, 6)
    assert_node(node, 48, 6)
    assert node.concat_val == 486
    assert node.multiply_val == 288
    assert node.plus_val == 54
    
    calculator = Calculator(156,[15,6])
    node = calculator.nodes[0]
    assert_node(node, 15, 6)
    assert node.plus_val == 21
    assert node.multiply_val == 90
    assert node.concat_val == 156

    calculator = Calculator(7290, [6,8])
    node = calculator.part_2_nodes[0]
    assert_node(node, 6, 8)

    calculator.add_part_2_layer(6)
    assert len(calculator.part_2_nodes) == 3
    nodes = calculator.part_2_nodes
    node_1 = nodes[0]
    node_2 = nodes[1]
    node_3 = nodes[2]

    assert_node(node_2, 48, 6)
    assert_node(node_1, 14, 6)
    assert_node(node_3, 68, 6)

    calculator = Calculator(7290,[6,8,6,15])
    assert calculator.calc_part_2() == True

    calculator = Calculator(192,[17, 8, 14])
    assert calculator.calc_part_2() == True


def test_calculate_part_2():

    assert calculate_part_2(sample_data) == 11387
    assert calculate_part_2(data) == 340362529351427
    # 3598853406210 too low
