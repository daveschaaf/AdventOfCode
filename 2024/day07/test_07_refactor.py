# Tests for 20204 Day 7 Refactor


# Test 2024 Day 7
import pytest
from refactor_07 import * 

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

def test_calibrate_pair():
    
    assert calibrate_pair(5,7, part = 1) == [12, 35]
    assert calibrate_pair(5,5, part = 1) == [10, 25]

    assert calibrate_pair(48, 6, part = 2) == [54, 288, 486]
    assert calibrate_pair(15, 6, part = 2) == [21, 90, 156]
    assert calibrate_pair(6, 8, part = 2) == [14, 48, 68]
    assert calibrate_pair(68, 6, part = 2) == [74, 408, 686]
    assert calibrate_pair(17, 8, part = 2) == [25, 136, 178]
    assert calibrate_pair(25, 14, part = 2) == [39, 350, 2514]
    assert calibrate_pair(136, 14, part = 2) == [150, 1904, 13614]
    assert calibrate_pair(178, 14, part = 2) == [192, 2492, 17814]

def test_calculate_part_1():
    assert calculate_part_1(sample_data) == 3749
    assert calculate_part_1(data) == 3598800864292

def test_calculate_part_2():
    assert calculate_part_2([[192, [17,8,14]]]) == 192
    assert calculate_part_2(sample_data) == 11387
    assert calculate_part_2(data) == 340362529351427
