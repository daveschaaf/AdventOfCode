# 2024 Day 9 Tests
import pytest

from sample_09 import *
from code09 import *

def test_create_block():
    assert create_block(sample1) == list(sample1_block)
    assert create_block(sample2) == list(sample2_block)
    assert create_block(sample3) == list(sample3_block)

def test_compact_block():
    assert compact_block(list(sample1_block)) == list(sample1_block_compact)
    assert compact_block(list(sample2_block)) == list(sample2_block_compact)
    assert compact_block(list(sample3_block)) == list(sample3_block_compact)

def test_checksum():
    assert checksum(list(sample1_block_compact)) == (
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
    assert checksum(list(sample3_block_compact)) == 1928
    assert checksum(list('00992111777.44.333....5555.6666.....8888..')) == 2858

def test_defrag_compact_block():
    def df_test(test_str, expectation):
        assert defrag_compact_block(list(test_str)) == list(expectation)
    df_test("0.1", "01.")
    df_test("0.1..22", "01.22..")
    df_test(sample3_block,'00992111777.44.333....5555.6666.....8888..')

def test_part1():
    assert part1(sample3) == 1928
    assert part1(part1_input) == 6346871685398
    # 5610071428 too low
    # 90273982836 too low

def test_part2():
    if DEBUG:
        return
    assert part2(part1_input) == 6373055193464
    # 6315254517968 too low
    # 6316105058804 too low
    # 6373055193464
    
