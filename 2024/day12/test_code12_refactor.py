import pytest
from code12_refactor import parse_map, Region, part1, part2
from data12 import *


def test_parse_map():
    parsed_map = parse_map(map1)
    assert len(parsed_map) == 4
    assert len(parsed_map[1]) == 4
    assert isinstance(parsed_map, list)
    assert isinstance(parsed_map[1], list)

parsed_map1 = parse_map(map1)

def assert_raw_map(raw_map, starting, area, perimeter, sides = None):
    parsed_map = parse_map(raw_map)
    region = Region(parsed_map, starting)
    assert region.area == area
    assert region.perimeter == perimeter
    assert region.price() == area * perimeter
    if sides is not None:
        assert region.sides == sides

def test_region_get_value():
    """it returns the value"""
    region = Region(parsed_map1, (0,0))
    assert region.get_value(*(0,0)) == "A"
    assert region.get_value(*(3,3)) == "C"
    """it return None for out of bounds"""
    assert region.get_value(*(99,99)) == None
    assert region.get_value(*(4,4)) == None

def test_region_plots():
    """it returns the coordinates of the plot cells"""
    region = Region(parsed_map1, (0,0))
    plots = region.plots
    assert isinstance(plots, set)
    assert len(plots) == 4
    assert (0,3) in plots
    assert (1,1) not in plots

def test_map_0():
    """it find the price of a single plot"""
    assert_raw_map("0", (0,0), 1, 4, 4)

def test_map_00():
    """it finds the price of a connected plot"""
    assert_raw_map("00", (0,0), 2, 6, 4)

def test_map_0000():
    """it finds the price of a plot on 2 rows"""
    assert_raw_map("00\n00", (0,0), 4, 8, 4)

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

def test_region_plot_corners():
    """it counts the correct sides for simple maps"""
    parsed_map = parse_map("0")
    cell = (0,0)
    region = Region(parsed_map, cell)
    assert region.sides == 4
    region = Region(parse_map("00"), cell)
    assert region.sides == 4
    region = Region(parse_map("000"), cell)
    assert region.sides == 4

def assert_region_sides(map, cell, sides):
    parsed_map = parse_map(map)
    region = Region(parsed_map, cell)
    assert region.sides == sides

def test_region_sides_outside():
    """it counts outside corners"""
    assert_region_sides(map1, (0,0), 4)
    assert_region_sides(map1, (1,0), 4)
    assert_region_sides(map1, (3,2), 4)

def test_region_sides_inside():
    """it counts inside corners"""
    assert_region_sides(map1, (2,2), 8)

def test_part1():
    """it returns the total price of the garden"""
    assert part1(map1) == 140
    assert part1(map2) == 772
    assert part1(map3) == 1930
    assert part1(puzzle)== 1485656

def test_part2():
    """it returns the discounted price of the garden"""
    assert part2(map1) == 80
    assert part2(map_e) == 236
    assert part2(map_ab) == 368
    assert part2(puzzle) == 899196
