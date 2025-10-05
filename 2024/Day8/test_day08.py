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

def map_sample_1(sample = sample_1):
    return AntennaMap(sample)

def test_parse_sample():
    map_1 = map_sample_1().map
    assert len(map_1) == 10
    assert len(map_1[0]) == 10
    assert map_1[1][3] == "#"
    assert map_1[3][4] == "a"
    assert map_1[5][5] == "a"
    assert map_1[7][6] == "#"


def test_find_antennas():
    map_1 = map_sample_1()
    antennas = map_1.find_antennas()
    assert (3,4) in map_1.find_antennas()
    assert (3,4) in map_1.antennas
    assert (5,5) in map_1.find_antennas()
    assert (5,5) in map_1.antennas

def test_set_get():
    map_1 = map_sample_1()

    assert map_1.set("@", 1,2) == "@"
    assert map_1.map[1][2] == "@"
    assert map_1.get(1,2) == "@"
    
    assert map_1.set("@", 100,2) == False
    assert map_1.get(100,2) == False
    
