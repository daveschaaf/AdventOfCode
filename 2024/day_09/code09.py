# 2024 Day 9 Code

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

def checksum(block):
    block = [int(n) for n in filter(lambda c: c != ".", block)]
    return sum([ i*block[int(i)] for i in range(len(block))])

def part1(input):
    block = create_block(input)
    compact = compact_block(block)
    return checksum(compact)
