## 2023 Day 3, Part 1

data:[list] = []

with open("03_data.txt", "r") as file:
    for line in file:
        data.append(list(line.replace('\n','')))

found_num: bool = False

num_start_list: [tuple] = []
current_num: int = 0
search_set: set = set()
parts: [int] = []

for i in range(len(data)):
    row: [str] = data[i]
    for j in range(len(row)):
        c = row[j]
        if not c.isnumeric():
            if found_num:
                # current_num is done
                # search for a symbol
                for tup in search_set:
                    char = data[tup[0]][tup[1]]
                    if char != '.' and not char.isnumeric():
                        # found a symbol
                        parts.append(current_num)
                        break
                search_set = set()
                found_num = False
                current_num = 0
        if c.isnumeric():
            if not found_num:
                # set the flag found_num = True
                found_num = True
                num_start_list.append((i, j))
            current_num = current_num*10 + int(c)
            for x in [i - 1, i, i + 1]:
                for y in [j - 1, j, j + 1]:
                    if x >= 0 and x <= 139 and y >= 0 and y <= 139:
                        search_set.add((x, y))

solution = sum(parts)

print("Solution to 2023 - Day 3, Part 1")
print(solution)
# 533775



## Part 2

star_parts: dict = {}
star_list: [tuple] = []

for i in range(len(data)):
    row: [str] = data[i]
    for j in range(len(row)):
        c = row[j]
 
        if c != "*":
            continue
        
        found_star: tuple = (i, j) 
        local_nums: set = set()
        
        #search for the nearby numbers
        for x in [i - 1, i, i + 1]:
            for y in [j - 1, j, j + 1]:
                
                check_condition: bool = False#i == 1 and j == 100

                if x >= 0 and x <= 139 and y >= 0 and y <= 139:
                    n = data[x][y]
                    if n.isnumeric():
                        current_num: int = n
                        
                        l = y - 1
                        # check numbers to the left
                        if check_condition:
                            print("Found number to check:")
                            print(f"{current_num=}")

                        while l >= 0 and data[x][l].isnumeric():
                            if check_condition:
                                print(f"{current_num=}")
                                print(f"next digit = {data[x][l]}")
                            current_num = data[x][l] + current_num
                            l -= 1
                        if check_condition:
                            print(f"num after l = {current_num}")

                        r = y + 1
                        while r <= 139 and data[x][r].isnumeric():
                            current_num = current_num + data[x][r]
                            r += 1
                        
                        local_nums.add(int(current_num))

        if len(local_nums) == 2:
            star_list.append(found_star)
            parts: [int] = list(local_nums)
            # print(parts)
            gear_ratio: int = parts[0] * parts[1]
            star_parts[found_star] = gear_ratio # set to gear ratio for solution
        elif len(local_nums) > 2:
            print(f"###Check this: {(x,y)}")
            print(local_nums)
        

# print(star_parts) 

solution: int = sum(star_parts.values())

print("Solution to 2023 Day 3, Part 2:")
print(solution)
# 78236071


## Part 2

