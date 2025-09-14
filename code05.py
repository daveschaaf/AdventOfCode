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

class ListNode():
    def __init__(self, val: int = None, next = None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self, rules: list[list[int]]):
        rule = rules[0]
        self.root: ListNode = ListNode(None,ListNode(rule[0],ListNode(rule[1],ListNode())))
    
    def add_rule(self, rule: list[int]):
        first: int = rule[0]
        second: int = rule[1]
        node: ListNode = self.root
        
        while node.next is not None:
            if second == node.next.val:
                new_node: ListNode = ListNode(first)
                old_next: ListNode = node.next
                new_node.next = old_next
                node.next = new_node
            node = node.next.next
        print(self)

    def __repr__(self):
        node: ListNode = self.root.next
        vals: list[int] = []
        while node.val:
            vals.append(str(node.val))
            node = node.next
        return "[" + ",".join(vals) + "]"


