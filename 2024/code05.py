# 2024 Day 5 Part 1
from collections import defaultdict

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

class ListNode():
    def __init__(self, val = None, prev = None, next = None):
        self.val: int | None = val
        self.next: ListNode | None = next
        self.prev: ListNode | None = prev

class LinkedList():
    def __init__(self, rules: list[list[int]]):
        self.size: int = 0
        self.root: ListNode = ListNode()
        self.tail: ListNode = ListNode()
        self.root.next = self.tail
        self.tail.prev = self.root
        self.vals: set = set()
        self.rules = []
        self.create_rules(rules.copy())

    def create_rules(self, rules) -> None:
        rule0: list[int] = rules[0]
        rule_first: int = rule0[0]
        rule_second: int = rule0[1]

        node0: ListNode = self.insert_between(rule_first, self.root, self.tail)
        self.insert_between(rule_second, node0, node0.next)
        self.rules.append(rule0)

        while len(rules) > 0:
            for rule in rules:
                if self.can_add_rule(rule):
                    self.add_rule(rule)
                    rules.remove(rule)

    def can_add_rule(self, rule) -> bool:
        return rule[0] in self.vals or rule[1] in self.vals

    def add_rule(self, rule) -> ListNode | None:
        rule_first: int = rule[0]
        rule_second: int = rule[1]
        has_first: bool = self.has_val(rule_first)
        has_second: bool = self.has_val(rule_second)

        if has_first and has_second:
            second_node: ListNode | None = self.get(rule_second)
            if not second_node:
                raise ValueError("node is None, expected ListNode")
            node: ListNode | None = second_node.next
            while node and node.val:
                if node.val == rule_first:
                    self.move_node(second_node, node, node.next)
                    break
                node = node.next
        elif has_first:
            node = self.get(rule_first)
            if not node:
                raise ValueError("node is None, expected ListNode")
            self.insert_between(rule_second, node, node.next)
        elif has_second:
            node = self.get(rule_second)
            if not node:
                raise ValueError("node is None, expected ListNode")
            self.insert_between(rule_first, node.prev, node)
        else:
            raise ValueError(f"Unable to add Rule {rule} into existing LinkedList")
        self.rules.append(rule)
        return node

    def move_node(self, node, prev, next) -> ListNode:
        node.prev.next = node.next
        node.next.prev = node.prev
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
        return node

    def insert_between(self, val, prev, next) -> ListNode:
        node = ListNode(val, prev, next)
        prev.next = node
        next.prev = node
        self.vals.add(val)
        self.size += 1
        return node

    def insert_list_between(self, linked_list, prev, next) -> ListNode:
        prev.next = linked_list.first
        linked_list.first.prev = prev
        linked_list.last.next = next
        next.prev = linked_list.last
        self.size += linked_list.size
        return prev.next

    def has_val(self, val) -> bool:
        return val in self.vals

    def get(self, val) -> ListNode | None:
        node: ListNode | None = self.first()
        while node:
            if node.val == val:
                return node
            else:
                node = node.next

    def first(self) -> ListNode | None:
        return self.root.next

    def last(self) -> ListNode | None:
        return self.tail.prev

    def __repr__(self) -> str:
        return str(self.as_list())

    def __len__(self) -> int:
        return self.size

    def as_list(self) -> list[int]:
        vals: list[int] = []
        node: ListNode | None = self.first()
        while node and node.val:
            vals.append(node.val)
            node = node.next
        return vals

    def __eq__(self, other) -> bool:
        if isinstance(other, LinkedList):
            other = other.as_list()
        if isinstance(other, list):
            this_list: list = self.as_list()
            if len(other) != len(self):
                return False
            for i in range(len(self)):
                if other[i] != this_list[i]:
                    return False
            return True
        else:
            return False

class UpdatePrinter():
    def __init__(self, updates: list[list[int]], rules: LinkedList ):
        self.rules: LinkedList = rules
        self.valid_updates: list[list[int]] = []
        if len(updates) > 0:
            self.validate_updates(updates)

    def validate_updates(self, updates: list[list[int]]) -> None:
        for update in updates:
            if self.validate(update):
                self.valid_updates.append(update)

    def validate(self, update: list[int]) -> bool:
        val_i: int = 0
        node: ListNode | None = self.rules.get(update[val_i])
        while node and node.val:
            if node.val == update[val_i]:
                val_i += 1
                if val_i == len(update):
                    return True
            node = node.next
        return False

    def part1(self):
        return sum([update[len(update) // 2] for update in self.valid_updates])

if __name__ == "__main__":
    parsed_rules, parsed_updates = create_full_dataset('05_data.dat')
    
    unique_rules: list[int] = list(set([item for sublist in parsed_rules.copy() for item in sublist]))
    rules_list: LinkedList = LinkedList([parsed_rules.copy()[0]])
    update_printer: UpdatePrinter = UpdatePrinter(parsed_updates, rules_list)

    while len(parsed_rules) > 0:
        for rule in parsed_rules:
            if rules_list.can_add_rule(rule):
                rules_list.add_rule(rule)
                update_printer = UpdatePrinter(rules_list.rules, rules_list)
                if update_printer.validate(rule) == False:
                    print('BROKE')
                    print(f"{rules_list=}")
                    print(f"{rule=}")
                    break
                parsed_rules.remove(rule)

    
    solution = update_printer.part1()
    
    print('2024 Day 5, Part 1 Solution:')
    print(solution)
