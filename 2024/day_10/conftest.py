import pytest
from sample10 import sample1, sample2, sample3, sample4, sample5, puzzle
from code10 import *


@pytest.fixture
def trailheads_paths_s1():
    return {(0,0): {((0,0), (0,1)), ((0,0), (1,0))}}


@pytest.fixture
def trailmap_s1():
    return parse_trailmap(sample1)
