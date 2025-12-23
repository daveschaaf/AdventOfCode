from collections import defaultdict

## Part 1

left = []
right = []

with open("01_data.txt", "r") as file:
    for line in file:

        val = line.split('   ')
        left.append(int(val[0]))
        right.append(int(val[1]))

left.sort()
right.sort()

solution1 = sum([abs(a - b) for a, b in zip(left, right)])

print('Solution to Day 1, Part 1:')
print(solution1)


## Part 2

freq = defaultdict(int)
left_hash = set(left)

for n in right:
    if n in left_hash:
        freq[n] += 1

solution2 = sum([k * v for k, v in freq.items()])

print('Solution to Day 1, Part 2:')
print(solution2)
