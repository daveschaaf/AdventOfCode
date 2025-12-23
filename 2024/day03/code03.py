# 2024 Day 3 Part 1

def valid_input(input):
    length: bool = len(input) <= 3
    numbers: bool = all([d.isnumeric() for d in input[:3]])
    return length and numbers

def mul(data):
    l: int = 0
    r: int = 0
    n: int = len(data)
    total: int = 0

    while r < n - 1:
        mul_idx: int = data.find('mul(', l)
        if mul_idx == -1:
            return total

        l = mul_idx + 4
        r = l + 1
        while data[r] != ")" and r < n:
            r += 1
        
        numbers: [str] = data[l:r].split(",")
        if len(numbers) != 2:
            continue

        input1: str = numbers[0]
        input2: str = numbers[1]
        if not (valid_input(input1) and valid_input(input2)):
            continue

        total += int(input1) * int(input2)
    return total


def mulnt(data):
    enabled: bool = True
    total: int = 0
    n: int = len(data)
    l: int = 0
    r: int = 0
    char_l: str = data[l]
    while l < n - 4:
        while char_l != "m" and char_l != "d" and l < n - 3:
            l += 1
            char_l = data[l]
        
        if data[l:l+4] == "mul(" and enabled:
            l = l + 4
            r = l + 1
            while data[r] != ")" and r < n:
                r += 1

            numbers: [str] = data[l:r].split(",")
            if len(numbers) != 2:
                continue

            input1: str = numbers[0]
            input2: str = numbers[1]
            if valid_input(input1) and valid_input(input2):
                print(f"{input1}*{input2} + ")
                total += int(input1) * int(input2)
            l = r + 1
        elif data[l:l+4] == 'do()':
            enabled = True
            l += 4
        elif data[l:l+7] == "don't()":
            enabled = False
            l += 7
        else:
            l += 1
    return total

def part2(data):
    dos: [str] = data.split('do()')
    dos = [do.split("don't()")[0] for do in dos]
    return sum([mul(do) for do in dos])
    

if __name__ == "__main__":
    data: str = ''
    with open('03_data.dat', "r") as file:
        
        for line in file:
            data += line

    solution1: int = mul(data)
    print("Solution to 2024 Day 4, Part1:")
    print(solution1)
    # 188192787

    solution2: int = part2(data)
    print("Solution to 2024 Day 4, Part 2:")
    print(solution2)
    # 114428878 too high < mulnt
    # 113908037 too low < mulnt
    # 113965544 < part2


