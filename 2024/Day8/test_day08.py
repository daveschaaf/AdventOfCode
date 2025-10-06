# 2024 Day 8 Tests
from day08 import *
import pytest

sample_1 = """..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
.........."""

sample_2 = """..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
.........."""


def map_sample(sample = sample_1):
    return AntennaMap(sample)


def test_parse_map():
    map_1 = map_sample().map
    assert len(map_1) == 10, 'has the correct number of rows'
    assert len(map_1[0]) == 10, 'has the correct number of columns'
    assert map_1[1][3] == "#", 'sets data in the correct position'
    assert map_1[3][4] == "a", 'sets data in the correct position'

    assert map_1[5][5] == "a", 'sets data in the correct position'

    assert map_1[7][6] == "#", 'sets data in the correct position'



def test_find_antennas():
    map_1 = map_sample()
    antennas = map_1.find_antennas()
    assert (3,4) in map_1.find_antennas(), "finds antennas on the map"
    assert (3,4) in map_1.antennas, "finds antennas on the map"
    assert (5,5) in map_1.find_antennas(), "finds antennas on the map"
    assert (5,5) in map_1.antennas, "finds antennas on the map"

def test_set_get():
    map_1 = map_sample()

    assert map_1.set("@", 1,2) == "@", 'sets a value within bounds'
    assert map_1.map[1][2] == "@", 'sets a value within bounds'
    assert map_1.get(1,2) == "@", 'accesses a value within bounds'
    
    assert map_1.set("@", 100,2) == False, 'does not set a value outside the rows'
    assert map_1.set("@", 2,200) == False, 'does not set a value outside the columns'
    assert map_1.get(100,2) == False, 'does not access a value outside the rows'
    assert map_1.get(2,200) == False, 'does not access a value outside the columns'

def test_set_antinodes():
    map_1 = map_sample()
    map_1.set_antinodes([(3,4),(5,5)],mark = "%")
    assert map_1.get(1,3) == "%"
    assert map_1.get(7,6) == "%"

    map_2 = map_sample(sample_2)
    assert map_2.get(3,4) == 'a'
    assert map_2.get(5,5) == 'a'
    assert map_2.get(4,8) == 'a'
    map_2.set_antinodes([(3,4),(5,5),(4,8)],mark = "%")
    assert map_2.get(1,3) == "%"
    assert map_2.get(7,6) == "%"
    assert map_2.get(2,0) == "%"
    assert map_2.get(6,2) == "%"

