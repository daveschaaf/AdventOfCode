## 2023 01
#  Part 1

data: [str] = []

with open("01_data.txt", "r") as file:
    for line in file:
        data.append(line)

def parse_calibration(str_list):

    calibration: [int] = []

    for string in str_list:
        digit_10: int = None
        digit_01: int = None

        r: int = len(string) - 1
        for l in range(len(string)):
            if digit_10 and digit_01:
                break

            if not digit_10 and string[l].isnumeric():
                digit_10 = int(string[l]) * 10

            if not digit_01 and string[r].isnumeric():
                digit_01 = int(string[r])
            else:
                r -= 1
        
        calibration.append(digit_10 + digit_01)

    return calibration

solution1: int = sum(parse_calibration(data))

print("Solution to 2023 Day 1, Part 1:")
print(solution1) # 55488



# Part 2
test_data= [
"two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"]

numbers = {"one": "1",
           "two": "2",
           "three": "3",
           "four": "4",
           "five": "5",
           "six": "6",
           "seven": "7",
           "eight": "8",
           "nine": "9",
           "1": "1",
           "2": "2",
           "3": "3",
           "4": "4",
           "5": "5",
           "6": "6",
           "7": "7",
           "8": "8",
           "9": "9"}

numbers_reversed = dict([(k[::-1], v) for k, v in numbers.items()])

cleaned_data: [str] = []

def replace_first(string, substring_hash):
    found = {}
    
    for k, v in substring_hash.items():
        location = string.find(k) 
        if location > -1:
            found[k] = location
    
    if not found:
        return string

    first_key = min(found, key= lambda x: found[x])
    
    return string.replace(first_key, substring_hash[first_key], 1)


for line in data: 
    line = replace_first(line, numbers)
    line = line[::-1]
    line = replace_first(line, numbers_reversed)
    line = line[::-1]
    cleaned_data.append(line)

with open('01_cleaned_data.txt', "w") as file:
    for line in cleaned_data:
        file.write(line)

solution2: int = sum(parse_calibration(cleaned_data))

print("Solution to 2023 Day 1, Part 2:")
print(solution2)
