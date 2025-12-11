# 2024 Day 10 Code

DEBUG = False

def debug(message):
    if DEBUG:
        print(message)

def trailheads(trailmap_input):
    trailmap = trailmap_input.split("\n")
    debug(trailmap)
    trailmap = [list(row) for row in list(filter(lambda c: c != "\n", trailmap))]
    debug(trailmap)
    n_rows = len(trailmap)
    n_cols = len(trailmap[0])
    zeros = set()
    for r in range(n_rows):
        for c in range(n_cols):
            if trailmap[r][c] == "0":
                zeros.add(tuple([r,c]))
    return zeros
