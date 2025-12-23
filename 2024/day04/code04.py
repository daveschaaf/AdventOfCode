# 2024 Day 4, Part 1


def find_as(data: str, m_idx: [int], vector: [int]):
    a_idx: [int] = m_idx.copy()
    s_idx: [int] = m_idx.copy()

    a_idx[0] += vector[0]
    a_idx[1] += vector[1]
    s_idx[0] += 2*vector[0]
    s_idx[1] += 2*vector[1]
    return get_data(data,a_idx[0],a_idx[1]) == 'A' and get_data(data,s_idx[0],s_idx[1]) == 'S'
    
def get_data(data,row,col):
    row_n: int = len(data) - 1
    col_n: int = len(data[0]) - 1
    if row < 0 or col < 0:
        return 0
    if row > row_n or col > col_n:
        return 0
    return data[row][col]

def parse_data(location):
    parsed: [list] = []
    with open(location, "r") as file:    
        for line in file:
            row: [str] = []
            for c in line:
                row.append(c)
            parsed.append(row)
    return parsed

def find_xmas(data: [list]):
    xmas: int = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "X":
                for r in range(row-1,row+2):
                    for c in range(col-1,col+2):
                        if get_data(data,r,c) == "M":
                            if find_as(data, [r,c], [r-row,c-col]):
                                xmas += 1
    return xmas

def check_m_s_corners(data, a_idx):
    a_row: int = a_idx[0]
    a_col: int = a_idx[1]
    mas: int = 0
    # Key: index offset of M position
    # Value: index offset of respective S position for opposite corner
    m_s: dict = {
        (-1,-1): (1, 1),
        (-1,1): (1,-1),
        (1,-1): (-1,1),
        (1,1): (-1,-1)
    }
    for m_idx, s_idx in m_s.items():
        m: str = get_data(data,a_row + m_idx[0],a_col + m_idx[1])
        if m != "M":
            continue
        s: str = get_data(data,a_row + s_idx[0],a_col + s_idx[1])
        if s != "S":
            continue
        mas += 1
    return mas == 2

def find_x_mas(data: [list]):
    x_mas: int = 0

    for row in range(1,len(data)-1):
        for col in range(1,len(data[0])-1):
            if data[row][col] == "A":
                if check_m_s_corners(data, (row,col)):
                    x_mas += 1
    return x_mas


