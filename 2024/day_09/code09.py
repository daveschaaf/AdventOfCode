# 2024 Day 9 Code

def create_block(disk_map):
    disk_ints = [int(i) for i in disk_map]
    first_data, disk_ints = disk_ints[0], disk_ints[1:]
    result = ["0"] * int(first_data)
    file_id = 1
    for num in range(0, len(disk_ints), 2):
        blank_space = disk_ints[num]
        file_space = disk_ints[num + 1]
        for _ in range(blank_space):
            result.append(".")
        for _ in range(file_space):
            result.append(str(file_id))
        file_id = (file_id + 1) % 10
    return "".join(result)


