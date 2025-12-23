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
