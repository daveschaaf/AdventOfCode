from collections import defaultdict
def parse_input(input):
    return list(map(int, input.split(" ")))

def blink(input_array):
    """If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1."""
    """If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone."""
    """If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone"""
    blinked_array = []
    for x in input_array:
        x_str = str(x)
        x_len = len(x_str)
        if x == 0:
            blinked_array.append(1)
        elif x_len % 2 == 0:
            blinked_len = x_len//2
            blinked_array.append(int(x_str[:blinked_len]))
            blinked_array.append(int(x_str[blinked_len:]))
        else:
            blinked_array.append(x*2024)
    return blinked_array

def blink_times(input_array, times):
    for _ in range(times):
        input_array = blink(input_array)
    return input_array

def blink_val(val):
    if val == 0:
        return [1]
    x_str = str(val)
    x_len = len(x_str)
    if x_len % 2 == 0:
        blinked_len = x_len//2
        return [int(x_str[:blinked_len]), int(x_str[blinked_len:])]
    else:
        return [val*2024]

class Blinker():
    def __init__(self, puzzle_input):
        self.puzzle_array = parse_input(puzzle_input)
        self.memory = {}

    def count_stones(self, val, times):
        # Base case - a sinlge stone
        if times == 0:
            return 1

        # hashable key
        current = (val, times)
        # check if we've calculated this key previously
        if current in self.memory:
            return self.memory[current]
        
        # find the next value after a blink 
        total = 0
        for stone in self.blink_val(val):
            # for each of the new stones, count the stones after them
            total += self.count_stones(stone, times - 1)
        # once calculated add the total to memory
        self.memory[current] = total
        return total

    def length_after_times(self, times):
        #add all the stone count for each values in the puzzle
        return sum([self.count_stones(stone, times) for stone in self.puzzle_array])
    
    def blink_val(self, val):
        if val == 0:
            return [1]
        x_str = str(val)
        x_len = len(x_str)
        if x_len % 2 == 0:
            blinked_len = x_len//2
            return [int(x_str[:blinked_len]), int(x_str[blinked_len:])]
        else:
            return [val*2024]
