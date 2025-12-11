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
    def assert_next_step(sample, expectation):
        assert next_step(*trailheads(sample))[0] == expectation

    assert_next_step(sample1, {(0,1),(1,0)})
    assert_next_step(sample2, {(1,3)})
