def parse_rules(rules: list[str]) -> list[list[int]]:
    parsed_rules: list[list[int]] = []
    for line in rules:
        parsed_rules.append([int(n) for n in line.split("|")])
    return parsed_rules

def parse_updates(updates: list[str]) -> list[list[int]]:
    parsed_updates: list[list[int]] = []
    for line in updates:
        parsed_updates.append([int(n) for n in line.split(",")])
    return parsed_updates

def create_full_dataset(filename) -> tuple[list[list[int]], list[list[int]]]:
    with open(filename, 'r') as file:
        raw_data: list[str] = [] 
        for line in file:
            raw_data.append(line.replace('\n', ''))
    rules: list[str] =  []
    updates: list[str] = []
    rules_done: bool = False

    for data in raw_data:
        if rules_done:
            updates.append(data)
        elif data == '':
            rules_done = True
        else:
            rules.append(data)

    parsed_rules: list[list[int]] = parse_rules(rules)
    parsed_rules.sort()
    parsed_updates:list[list[int]] = parse_updates(updates)

    return parsed_rules, parsed_updates



def validate(update, rules):
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue
        first_i = update.index(rule[0])
        try:
            update.index(rule[1], first_i)
        except ValueError:
            return False
    return True





if __name__ == "__main__":
    rules , updates = create_full_dataset('05_data.dat')

    valid_updates = []
    invalid_updates = []
    
    for update in updates:
        if validate(update, rules):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

        
    print(len(updates))
    print(len(valid_updates))
    print(len(invalid_updates))
    print(sum(u[len(u) // 2] for u in valid_updates))
    # 7951  high
