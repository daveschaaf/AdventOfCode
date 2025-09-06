# Part 1

from code04 import find_x, find_m, find_as, find_xmas

xmas1 = [
    [".",".","X",".",".","."],
    [".","S","A","M","X","."],
    [".","A",".",".","A","."],
    ["X","M","A","S",".","S"],
    [".","X",".",".",".","."]
]
     
def test_find_x():
    # returns the index of the next X
    assert find_x(["X"]) == 0
    assert find_x(["X","X"]) == 0
    assert find_x([".","X"]) == 1
    assert find_x([".",".","."]) == -1
    assert find_x(xmas1[0]) == 2

def test_find_m():
    # return the index of the next M
    assert find_m(["M"]) == 0
    assert find_m(["M","M"]) == 0
    assert find_m([".","M"]) == 1
    assert find_m([".",".","."]) == -1
    assert find_m(xmas1[1]) == 3

def test_find_as():
    assert find_as(xmas1, [1,3], [1,1]) == True
    assert find_as(xmas1, [1,3], [0,-1]) == True
    assert find_as(xmas1, [3,1], [0,1]) == True
    assert find_as(xmas1, [3,1], [-1,0]) == True

def test_find_xmas():
    # return the number of XMAS found
    assert find_xmas("XM") == True
    assert find_xmas(xmas1) == 4
