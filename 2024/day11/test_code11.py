import pytest
from code11 import parse_input, blink, blink_times, blink_val, Blinker


sample1 = "0 1 10 99 999"
sample2 = "125 17"

def test_parse_input():
    result = parse_input(sample1)
    assert len(result) == 5
    assert isinstance(result, list)
    assert result == [0, 1, 10, 99, 999]

def blinked(input):
    parsed = parse_input(input)
    result = blink(parsed)
    return result

def test_rule_1():
    """If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1."""
    result = blinked(sample1)
    assert result[0] == 1
def test_rule_2():
    """If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone"""
    result = blinked(sample1)
    assert result[1] == 2024
    assert result[6] == 2021976
def test_rule_3():
    """If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone."""
    result = blinked(sample1)
    assert result[2] == 1
    assert result[3] == 0
    assert result[4] == 9
    assert result[5] == 9

blink_series = """125 17
253000 1 7
253 0 2024 14168
512072 1 20 24 28676032
512 72 2024 2 0 2 4 2867 6032
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2"""
blink_series_inputs = blink_series.split("\n")
blink_series_result = [list(map(int,t.split(" "))) for t in blink_series_inputs]
start = [125, 17]
def test_blink_one_time():
    assert start == blink_series_result[0]
    assert blink(start) == blink_series_result[1]

def test_blink_two_times():
    assert blink(blink(start)) == blink_series_result[2]
    assert blink_times(start, 2) == blink_series_result[2]

def test_blink_n_times():
    for i in range(3, 7):
        assert blink_times(start, i) == blink_series_result[i]

puzzle = "1750884 193 866395 7 1158 31 35216 0"
puzzle_array = parse_input(puzzle)
def test_part1():
    assert len(blink_times(puzzle_array, 25)) == 231278

def test_blink_val():
    """It returns an array that follows the rules for a single val"""
    assert blink_val(125) == [253000]
    assert blink_val(17) == [1,7]
    assert blink_val(253000) == [253, 0]
    assert blink_val(0) == [1]

def test_part2():
    blinker = Blinker(puzzle)
    assert blinker.length_after_times(25) == 231278 
    assert blinker.length_after_times(75) == 274229228071551

