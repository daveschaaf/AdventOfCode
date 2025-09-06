# 2024 Day 4, Part 1

def find_x(data: str):
    for i in range(len(data)):
        if data[i] == "X":
            return i
    return -1

def find_m(data: str):
    for i in range(len(data)):
        if data[i] == "M":
            return i
    return -1

def find_xmas(data: str):
    row_n: int = len(data)
    col_n: int = len(data[0])
    m_stack: [int] = []
    xmas: int = 0
    for row in range(row_n):
        for col in range(col_n):
            if data[row][col] == "X":
                print(f"Found X at: {row},{col}")
                for r in range(row-1,row+2):
                    if r < 0 or r > row_n -1:
                        continue
                    for c in range(col-1,col+2):
                        if c < 0 or c > col_n -1:
                            continue
                        print(data[r][c])
                        if data[r][c] == "M":
                            print(f"Found M at :{r},{c}")
                            xmas += 1
    return xmas


