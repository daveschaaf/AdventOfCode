# 2024 Day 9 Tests
import pytest

from sample_09 import *
from code09 import *

def test_create_block():
    assert create_block(sample1) == sample1_block
    assert create_block(sample2) == sample2_block
    assert create_block(sample3) == sample3_block

def test_compact_block():
    assert compact_block(sample1_block) == sample1_block_compact
    assert compact_block(sample2_block) == sample2_block_compact
    assert compact_block(sample3_block) == sample3_block_compact

def test_checksum():
    assert checksum(sample1_block_compact) == (
            0*0 +
            1*2 +
            2*2 +
            3*1 +
            4*1 +
            5*1 +
            6*2 +
            7*2 +
            8*2
    )
    assert checksum(sample3_block_compact) == 1928

def test_part1():
    assert part1(part1_input) == -1
    # 5610071428 too low
