# 2024 Day 9 Code
DEBUG = True

def debug(message):
    if not DEBUG: pass
    if isinstance(message, list):
        print("".join(message))
    print(message)

def create_block(disk_map):
    disk_ints = [int(i) for i in disk_map]
    first_data, disk_ints = disk_ints[0], disk_ints[1:]
    block = ["0"] * int(first_data)
    file_id = 1
    for i in range(0, len(disk_ints), 2):
        blank_space = disk_ints[i]
        file_space = disk_ints[i + 1]
        for _ in range(blank_space):
            block.append(".")
        for _ in range(file_space):
            block.append(str(file_id))
        file_id += 1
    return block

def compact_block(block):
    l = 0
    r = len(block) - 1
    while l < r-1:
        if block[l] == ".":
            while block[r] == ".":
                r -= 1
            block[l], block[r] = block[r], block[l]
        l += 1
    return block

def defrag_compact_block(block):
    block.append(".")
    last_i = len(block) - 1
    r = last_i
    debug(f"Start block: {"".join(block)}")
    while r > 0:
        while block[r] == ".":
            r -= 1
        debug(f"{r=}")
        file_id = block[r]
        file_end = r+1
        debug(f"{file_end=}")
        while block[r] == file_id:
            r -= 1
        file_start = r+1
        debug(f"{file_start=}")
        file_len = file_end - file_start
        debug(f"{block[file_start:file_end]}")
        l = 0
        while l < r:
            while block[l] != "." and l < r - 1 :
                l += 1
            free_start = l
            while block[l] == "." and l < r - 1:
                l += 1
            free_end = l
            free_len = free_end - free_start
            if free_len >= file_len:
                free_end = free_start + file_len
                block[free_start:free_end] = block[file_start:file_end]
                block[file_start:file_end] = ["."]*file_len
                debug(f"Swapped block: {"".join(block)}")
                l = r
            l += 1
    block.pop()
    return block

def checksum(block):
    block = [ 0 if n == "." else int(n) for n in block ]    
    return sum(i*v for i, v in enumerate(block))

def part1(input):
    block = create_block(input)
    compact = compact_block(block)
    return checksum(compact)
