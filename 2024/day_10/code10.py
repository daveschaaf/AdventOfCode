# 2024 Day 10 Code

DEBUG = True

def debug(message):
    if DEBUG:
        print(message)


def parse_trailmap(trailmap_input):
    trailmap = trailmap_input.split("\n")
    trailmap = [list(row) for row in list(filter(lambda c: c != "\n", trailmap))]
    return trailmap


def trailheads(trailmap):
    n_rows = len(trailmap)
    n_cols = len(trailmap[0])
    zeros = dict()
    for r in range(n_rows):
        for c in range(n_cols):
            if trailmap[r][c] == "0":
                loc = tuple([r,c])
                zeros[loc] = next_step(loc, trailmap, "1")
    return zeros, trailmap

def travel(trails, trailmap):
    any_trailpoint = list(list(trails.values())[0])[0]
    current_val = int(trailmap[any_trailpoint[0]][any_trailpoint[1]])
    next_val = str(current_val + 1)
    for origin, paths in trails.items():
        steps = set()
        for path in paths:
            path_steps = next_step(path, trailmap, next_val)
            steps.update(path_steps)
        trails[origin] = steps
    return trails, trailmap

def next_step(path, trailmap, next_val):
    r_bound = len(trailmap)
    c_bound = len(trailmap[0])
    steps = set()
    step_options = [(path[0]+1,path[1]),(path[0],path[1]+1),
                    (path[0]-1,path[1]),(path[0],path[1]-1)]
    for step in step_options:
        r = step[0]
        c = step[1]
        if (r>=0 and r<r_bound) and (c>=0 and c<c_bound):
            if trailmap[r][c] == next_val:
                steps.add(tuple([r,c]))
    return steps


def score(trailmap_input):
    debug("#################")
    positions, trailmap = trailheads(trailmap_input)
    for n in range(8):
        positions, trailmap = next_step(positions, trailmap)
        debug(f"{n+1} = {positions}")
    nines = sum([len(paths) for paths in positions.values()])
    return nines
