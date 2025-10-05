# 2024 Day 7 Refactor


sample = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def parse_sample(sample):
    lines = sample.split("\n")
    lines_split = [line.split(": ") for line in lines]
    line_list = [ [int(line[0]), [int(n) for n in line[1].split(" ")]] for line in lines_split]
    return line_list

def parse_data(file):
    line_list = []
    for line in file:
        line = line.replace("\n",'')
        line_split = line.split(": ")
        line_list.append([int(line_split[0]), [int(n) for n in line_split[1].split(" ")]])
    return line_list

data = parse_sample(sample)



def calculate_part_1(data):
    result = 0
    for line in data:
        target = line[0]
        numbers = line[1]

        calibrated_numbers = calibrate_pair(numbers[0], numbers[1], 1)
        
        for raw_num in numbers[2:]:
            recalibrated = []
            for calced_num in calibrated_numbers:
                recalibrated = recalibrated + calibrate_pair(calced_num, raw_num)
            calibrated_numbers = recalibrated

        if target in calibrated_numbers:
            result += target
    return result


def calibrate_pair(num_1, num_2, part = 1):
    add = num_1 + num_2
    multiply = num_1 * num_2
    if part > 1:
        concat = int(str(num_1) + str(num_2))
        return [add, multiple, concat]
    return [add, multiply]

