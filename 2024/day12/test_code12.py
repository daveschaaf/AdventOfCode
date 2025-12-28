import pytest
from code12 import parse_map, Region





map1 = """AAAA
BBCD
BBCC
EEEC"""

def test_parse_map():
    parsed_map = parse_map(map1)
    print(parsed_map)
    assert len(parsed_map) == 4
    assert len(parsed_map[1]) == 4
    assert isinstance(parsed_map, list)
    assert isinstance(parsed_map[1], list)

parsed_map1 = parse_map(map1)

def assert_raw_map(raw_map, starting, area, perimeter):
    parsed_map = parse_map(raw_map)
    region = Region(parsed_map, starting)
    assert region.area == area
    assert region.perimeter == perimeter
    assert region.price() == area * perimeter

def test_region_get_value():
    """it returns the value"""
    region = Region(parsed_map1, (0,0))
    assert region.get_value(*(0,0)) == "A"
    assert region.get_value(*(3,3)) == "C"
    """it return None for out of bounds"""
    assert region.get_value(*(99,99)) == None
    assert region.get_value(*(4,4)) == None

def test_map_0():
    """it find the price of a single plot"""
    assert_raw_map("0", (0,0), 1, 4)

def test_map_00():
    """it finds the price of a connected plot"""
    assert_raw_map("00", (0,0), 2, 6)

def test_map_0000():
    """it finds the price of a plot on 2 rows"""
    assert_raw_map("00\n00", (0,0), 4, 8)

def test_map_0011():
    """it finds the price of a garden with multiple plots"""
    assert_raw_map("00\n11", (0,0), 2, 6)
    assert_raw_map("00\n11", (1,1), 2, 6)

def test_map1_A():
    """it finds the A of the first garden map"""
    assert_raw_map(map1, (0,0), 4, 10)

def test_map1_b():
    """it finds the B of the first garden map"""
    assert_raw_map(map1, (1,0), 4, 8)

def test_map1_c():
    """it finds the C of the first garden map"""
    assert_raw_map(map1, (2,2), 4, 10)

def test_map1_E():
    """it finds the E of the first garden map"""
    assert_raw_map(map1, (3,2), 3, 8)
