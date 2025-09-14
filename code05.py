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
    def __init__(self, val: int = None, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList():     
    def __init__(self, rules: list[list[int]]):
        self.size: int = 0
        self.root: ListNode = ListNode()
        self.tail: ListNode = ListNode()
        self.root.next = self.tail
        self.tail.prev = self.root
        self.vals: set = set()
        self.create_rules(rules)


    def create_rules(self, rules):
        rule0: list[int] = rules.pop()
        rule_first: int = rule0[0]
        rule_second: int = rule0[1]
        
        node0: ListNode = self.insert_between(rule_first, self.root, self.tail)
        self.insert_between(rule_second, node0, node0.next)

        while len(rules) > 0:
            for rule in rules:
                if self.can_add_rule(rule):
                    self.add_rule(rule)
                    rules.remove(rule)

    def can_add_rule(self, rule):
        return rule[0] in self.vals or rule[1] in self.vals

    def add_rule(self, rule):
        rule_first: int = rule[0]
        rule_second: int = rule[1]

        if self.has_val(rule_first) and self.has_val(rule_second):
            second_node: ListNode = self.get(rule_second)
            node: ListNode = second_node.next
            while node.val:
                if node.val == rule_first:
                    self.move_node(node, second_node.prev, second_node)
                    break
                node = node.next
        elif self.has_val(rule_first):
            node = self.get(rule_first)
            self.insert_between(rule_second, node, node.next)
        elif self.has_val(rule_second):
            node = self.get(rule_second)
            self.insert_between(rule_first, node.prev, node)
        else:
            raise ValueError(f"Unable to add Rule {rule} into existing LinkedList")
        return node

    def move_node(self, node, prev, next):
        node.prev.next = node.next
        node.next.prev = node.prev
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def insert_between(self, val, prev, next):
        node = ListNode(val, prev, next)
        prev.next = node
        next.prev = node
        self.vals.add(val)
        self.size += 1
        return node

    def insert_list_between(self, linked_list, prev, next):
        prev.next = linked_list.first
        linked_list.first.prev = prev
        linked_list.last.next = next
        next.prev = linked_list.last
        self.size += linked_list.size
        return prev.next

    def has_val(self, val):
        return val in self.vals

    def get(self, val):
        node: LinkedList = self.root.next
        while node:
            if node.val == val:
                return node
            else:
                node = node.next
        return None

    def first(self):
        return self.root.next
    def last(self):
        return self.tail.prev

    def __repr__(self):
        return str(self.as_list())

    def __len__(self):
        return self.size

    def as_list(self):
        vals: [int] = []
        node = self.first()
        while node.val:
            vals.append(node.val)
            node = node.next
        return vals
    
    def __eq__(self, other):
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
