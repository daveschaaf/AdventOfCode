# 2024 Day 5 Part 1

def parse_rules(rules: str):
    rules = rules.split('\n')
    parsed_rules: list[list[int]] = []
    for line in rules:
        parsed_rules.append([int(n) for n in line.split("|")])
    return parsed_rules

def parse_updates(updates):
    updates = updates.split('\n')
    parsed_updates: list[list[int]] = []
    for line in updates:
        parsed_updates.append([int(n) for n in line.split(",")])
    return parsed_updates
