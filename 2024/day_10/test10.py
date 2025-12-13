# 2024 Day 10 Tests
import pytest
from code10 import *
from sample10 import *

def test_trailheads():
    assert trailheads(parse_trailmap(sample1))[0] == {(0,0): set([(0,1),(1,0)])}
    assert trailheads(parse_trailmap(sample2))[0] == {(0,3): set([(1,3)])}
    assert trailheads(parse_trailmap(sample3))[0] == {(0,3): set([(1,3)])}
    assert trailheads(parse_trailmap(sample4))[0] == {(0,1): set([(0,0)]),(6,5): set([(6,6)])}


def test_parse_trailmap():
    sample5_trailmap = parse_trailmap(sample5)
    assert isinstance(sample5_trailmap,list)
    assert len(sample5_trailmap) == 8
    assert len(sample5_trailmap[0]) == 8


def test_next_step():
    trailmap = parse_trailmap(sample1)
    _, trailmap = trailheads(trailmap)
    steps1 = next_step((0,0), trailmap, "1")
    expectation = set([(0,1),(1,0)])
    assert steps1 == expectation

    steps2_0 = next_step((0,1), trailmap, "2")
    assert steps2_0 == set([(0,2),(1,1)])

    steps2_1 = next_step((1,0), trailmap, "2")
    assert steps2_1 == set([(1,1)])


def test_travel():
    def assert_travel(sample, expectation):
        trailmap = parse_trailmap(sample)
        trails, trailmap = trailheads(trailmap)
        assert trails == expectation[0]
        for n in range(1,9):
            trails, trailmap = travel(trails, trailmap)
            assert trails == expectation[n]


    # Find the 1s
    assert_travel(sample1, [    {(0,0):set([(0,1),(1,0)])},
                                {(0,0):set([(0,2),(1,1)])},
                                {(0,0):set([(0,3),(1,2)])},
                                {(0,0):set([(1,3)])},
                                {(0,0):set([(2,3)])},
                                {(0,0):set([(2,2),(3,3)])},
                                {(0,0):set([(2,1),(3,2)])},
                                {(0,0):set([(2,0),(3,1)])},
                                {(0,0):set([(3,0)])}
                               ])


def test_score():
    assert score({(0,0):set([(2,3)])}) == 1
    assert score({(0,0):set([(2,0),(3,1)])}) == 2
    assert score({(0,1): set([(0,0)]),(6,5): set([(6,6)])}) == 2
    

def test_part1():
    assert part1(sample1) == 1
    assert part1(sample2) == 2
    assert part1(sample3) == 4
    assert part1(sample4) == 3
    assert part1(sample5) == 36
    assert part1(puzzle) == 512

