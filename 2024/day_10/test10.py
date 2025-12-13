# 2024 Day 10 Tests
import pytest
from code10 import *
from sample10 import sample1, sample2, sample3, sample4, sample5, puzzle


@pytest.mark.parametrize("sample, expected_output", [
    # (sample_input, expected_output)
    (sample1, {(0,0): set([(0,1),(1,0)])}),
    (sample2, {(0,3): set([(1,3)])}),
    (sample3, {(0,3): set([(1,3)])}),
    (sample4, {(0,1): set([(0,0)]),(6,5): set([(6,6)])}),
])
def test_trailheads(sample, expected_output):
    """trailheads returns the locations of 0 for part 1"""
    trailmap = parse_trailmap(sample)
    assert trailheads(trailmap) == expected_output

def test_trailheads_for_paths(trailheads_paths_s1):
    """trailheads_for_paths returns the full path for part 2"""
    trailmap = parse_trailmap(sample1)
    trails = trailheads_for_paths(trailmap)
    assert trails == trailheads_paths_s1

def test_parse_trailmap():
    """it returns a list of rows and columns"""
    sample5_trailmap = parse_trailmap(sample5)
    assert isinstance(sample5_trailmap,list)
    assert len(sample5_trailmap) == 8
    assert len(sample5_trailmap[0]) == 8


def test_next_step():
    """it finds all the orthogonally connected digits in squential order"""
    trailmap = parse_trailmap(sample1)
    steps1 = next_step((0,0), trailmap, "1")
    expectation = set([(0,1),(1,0)])
    assert steps1 == expectation

    steps2_0 = next_step((0,1), trailmap, "2")
    assert steps2_0 == set([(0,2),(1,1)])

    steps2_1 = next_step((1,0), trailmap, "2")
    assert steps2_1 == set([(1,1)])


def test_travel(trailmap_s1):
    """it updated the current location on the path uniquely"""
    expected_steps = [  {(0,0):set([(0,1),(1,0)])},
                        {(0,0):set([(0,2),(1,1)])},
                        {(0,0):set([(0,3),(1,2)])},
                        {(0,0):set([(1,3)])},
                        {(0,0):set([(2,3)])},
                        {(0,0):set([(2,2),(3,3)])},
                        {(0,0):set([(2,1),(3,2)])},
                        {(0,0):set([(2,0),(3,1)])},
                        {(0,0):set([(3,0)])}
                    ]
    current_trails = trailheads(trailmap_s1)
    assert current_trails == expected_steps[0]

    for n in range(1, len(expected_steps)):
        current_trails = travel(current_trails, trailmap_s1)
        assert current_trails == expected_steps[n]

def test_travel_path(trailheads_paths_s1, trailmap_s1):
    """it tracks the full unique paths at the next step"""
    expectation = {(0,0): {
                                ((0,0), (0,1), (0,2)), 
                                ((0,0), (0,1), (1,1)),                        
                                ((0,0), (1,0), (1,1))
                              }
                      }
    assert travel_path(trailheads_paths_s1, trailmap_s1, "2") == expectation 

def test_score():
    """it calcualtes the number of elements in the set per origin point"""
    assert score({(0,0):set([(2,3)])}) == 1
    assert score({(0,0):set([(2,0),(3,1)])}) == 2
    assert score({(0,1): set([(0,0)]),(6,5): set([(6,6)])}) == 2
    # part 2
    assert score({
        (0,1): { ((0,1),), ((1,0),) },
        (6,5): { ((6,6),) }
    }) == 3

def test_part1():
    """it calculates the correct score for each origin point"""
    assert part1(sample1) == 1
    assert part1(sample2) == 2
    assert part1(sample3) == 4
    assert part1(sample4) == 3
    assert part1(sample5) == 36
    assert part1(puzzle) == 512

def test_part2():
    """it calculates the correct number of unique paths for given the input"""
    assert part2(sample5) == 81
    assert part2(puzzle) == 1045
