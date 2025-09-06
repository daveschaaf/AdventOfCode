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
    return find_x(data) >= 0 and find_m(data)>= 0  


