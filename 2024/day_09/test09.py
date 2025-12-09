# 2024 Day 9 Tests
import pytest

from sample_09 import *
from code09 import *

def test_create_block():
    assert create_block(sample1) == sample1_block
    assert create_block(sample2) == sample2_block
    assert create_block(sample3) == sample3_block



