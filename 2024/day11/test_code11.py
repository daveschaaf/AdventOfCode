from code11 import parse_input, blink


sample1 = "0 1 10 99 999"

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
