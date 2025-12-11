# 2024 Day 10 Tests

from code10 import *
from sample10 import *

def test_trailheads():
    assert trailheads(sample1)[0] == {(0,0)}
    assert trailheads(sample2)[0] == {(0,3)}
    assert trailheads(sample3)[0] == {(0,3)}
    assert trailheads(sample4)[0] == {(0,1),(6,5)}
    assert trailheads(sample5)[0] == {(0,2),(2,4),(5,5),(0,4),
                                   (7,1),(4,6),(5,2),(6,6),(6,0)}

def test_next_step():
    def assert_next_step(sample, expectation, value):
        locs, trailmap = next_step(*trailheads(sample))
        for loc in iter(locs):
            assert loc in expectation
            assert trailmap[loc[0]][loc[1]] == str(value)
    
    # Find the 1s
    assert_next_step(sample1, [(0,1),(1,0)], 1)
    assert_next_step(sample2, [(1,3)], 1)

    assert_next_step(sample5, [(0,3),(0,5),(5,6),(1,2),(6,1),
                               (7,0),(1,4),(6,7),(5,3)], 1)

def test_score():
    assert score(sample1) == 1
    assert score(sample2) == 2
    assert score(sample3) == 4
    assert score(sample4) == 3
    # assert score(sample5) == 36


