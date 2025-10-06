# 2024 Day 8 Tests
from day08 import *
from samples08 import *
import pytest


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
    assert isinstance(map_1.find_antennas(), dict)
    assert (3,4) in map_1.antennas['a'], "finds antennas on the map"
    assert (5,5) in map_1.antennas['a'], "finds antennas on the map"

    map_3 = AntennaMap(sample_3)
    assert len(map_3.antennas) == 2
    
    antennas_0 = map_3.antennas["0"]
    assert len(antennas_0) == 4
    assert (1,8) in antennas_0, "finds antennas on the map"
    assert (2,5) in antennas_0, "finds antennas on the map"
    assert (3,7) in antennas_0, "finds antennas on the map"
    assert (4,4) in antennas_0, "finds antennas on the map"

    antennas_A = map_3.antennas["A"]
    assert len(antennas_A) == 3
    assert (5,6) in antennas_A, "finds antennas on the map"
    assert (8,8) in antennas_A, "finds antennas on the map"
    assert (9,9) in antennas_A, "finds antennas on the map"

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
    map_1.set_antinodes('a', [(3,4),(5,5)],mark = "%")
    assert map_1.get(1,3) == "%"
    assert map_1.get(7,6) == "%"

    map_2 = map_sample(sample_2)
    assert map_2.get(3,4) == 'a'
    assert map_2.get(5,5) == 'a'
    assert map_2.get(4,8) == 'a'
    map_2.set_antinodes('a', [(3,4),(5,5),(4,8)],mark = "%")

    assert map_2.get(1,3) == "%"
    assert map_2.get(7,6) == "%"
    assert map_2.get(2,0) == "%"
    assert map_2.get(6,2) == "%"
    
    map_3 = map_sample(sample_3)

    map_3.set_antinodes('A', map_3.antennas["A"], mark = "%")
    assert len(map_3.antinodes["A"]) == 5
    assert (7,7) in map_3.antinodes["A"]
    assert (10,10) in map_3.antinodes["A"]
    assert (11,10) in map_3.antinodes["A"]
    assert (2,4) in map_3.antinodes["A"]
    assert (1,3) in map_3.antinodes["A"]
    
    map_3.set_antinodes('0', map_3.antennas["0"], mark = "%")
    assert len(map_3.antinodes["0"]) == 10
    assert (0,6) in map_3.antinodes["0"]
    assert (0,11) in map_3.antinodes["0"]
    assert (1,3) in map_3.antinodes["0"]
    assert (2,10) in map_3.antinodes["0"]
    assert (3,2) in map_3.antinodes["0"]
    assert (4,9) in map_3.antinodes["0"]
    assert (5,1) in map_3.antinodes["0"]
    assert (5,6) in map_3.antinodes["0"]
    assert (6,3) in map_3.antinodes["0"]
    assert (7,0) in map_3.antinodes["0"]

def test_part_1():
    assert map_sample(sample_1).part_1() == 2
    assert map_sample(sample_2).part_1() == 4
    assert map_sample(sample_3).part_1() == 14
    assert map_sample(fulldata).part_1() == 354

def test_part_2():
    map_part_2 = map_sample(sample_part_2)

    
    assert map_sample(sample_part_2).part_2() == 6
    assert map_sample(fulldata).part_2() == -1
    #1131 too low

