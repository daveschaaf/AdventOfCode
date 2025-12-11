# 2024 Day 10 Code

DEBUG = True

def debug(message):
    if DEBUG:
        print(message)

def trailheads(trailmap_input):
    trailmap = trailmap_input.split("\n")
    trailmap = [list(row) for row in list(filter(lambda c: c != "\n", trailmap))]
    n_rows = len(trailmap)
    n_cols = len(trailmap[0])
    zeros = set()
    for r in range(n_rows):
        for c in range(n_cols):
            if trailmap[r][c] == "0":
                zeros.add(tuple([r,c]))
    return zeros, trailmap

def next_step(trails, trailmap):
    steps = set()
    r_bound = len(trailmap)
    c_bound = len(trailmap[0])
    any_trailpoint = next(iter(trails))
    current_val = int(trailmap[any_trailpoint[0]][any_trailpoint[1]])
    next_val = str(current_val + 1)
    for path in trails:
        step_options = [(path[0]+1,path[1]),(path[0],path[1]+1),
                        (path[0]-1,path[1]),(path[0],path[1]-1)]
        debug(f"{step_options=}")
        for step in step_options:
            r = step[0]
            c = step[1]
            if (r>=0 and r<r_bound) and (c>=0 and c<c_bound):
                if trailmap[r][c] == next_val:
                    debug(f"{step} = {next_val}")
                    steps.add(tuple([r,c]))
    return steps, trailmap
        
