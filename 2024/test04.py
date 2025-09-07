# Part 1

from code04 import  find_as, find_xmas, get_data, parse_data, find_x_mas, check_m_s_corners

xmas1 = [
    [".",".","X",".",".","."],
    [".","S","A","M","X","."],
    [".","A",".",".","A","."],
    ["X","M","A","S",".","S"],
    [".","X",".",".",".","."]
]

xmas2 = parse_data('04_data.dat')

xmas3 = [
    [".",".","X",".",".","."],
    [".","S","A","M","X","M"],
    [".","A",".",".","A","."],
    ["X","M","A","S",".","S"],
    [".","X",".",".",".","."]
]

def test_parse_data():
    assert len(xmas2) == 140
    assert len(xmas2[0]) == 141
    assert xmas2[0][0] == "X"
    assert xmas2[8][31] == "M"
    assert xmas2[40][133] == "A"
    assert xmas2[42][135] == "S"

     
def test_find_as():
    assert find_as(xmas1, [1,3], [1,1]) == True
    assert find_as(xmas1, [1,3], [0,-1]) == True
    assert find_as(xmas1, [3,1], [0,1]) == True
    assert find_as(xmas1, [3,1], [-1,0]) == True

def test_get_data():
    assert get_data(xmas1,0,0) == "."
    assert get_data(xmas1,5,0) == 0
    assert get_data(xmas1,0,6) == 0
    assert get_data(xmas1,0,2) == "X"
    assert get_data(xmas1,0,0) == "."
    assert get_data(xmas1,0,3) == "."
    assert get_data(xmas1,3,1) == "M"
    assert get_data(xmas1,2,4) == "A"
    assert get_data(xmas1,3,5) == "S"

def test_find_xmas():
    # return the number of XMAS found
    assert find_xmas(xmas1) == 4
    assert find_xmas(xmas2) == 2500


def test_check_m_s_corners():
    assert check_m_s_corners(xmas3, (2,4)) == True
    assert check_m_s_corners(xmas1, (2,4)) == False

def test_find_x_mas():
    assert find_x_mas(xmas3) == 1
    assert find_x_mas(xmas2) == 1933
