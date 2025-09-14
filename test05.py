# 2024 Day 5 Test
from code05 import *

rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

updates = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

parsed_rules = parse_rules(rules)
parsed_updates = parse_updates(updates)


def test_parse_rules():
    assert len(parsed_rules) == 21
    assert parsed_rules[0] == [47,53]
    assert parsed_rules[-1] == [53,13]

def test_parse_updates():
    assert len(parsed_updates) == 6
    assert parsed_updates[0] == [75,47,61,53,29]
    assert parsed_updates[-1] == [97,13,75,29,47]

def test_rules():
    linked_list_0: Linkedlist = LinkedList([[47,53]])
    assert linked_list_0.root.val == None
    assert linked_list_0.root.next.val == 47
    assert linked_list_0.root.prev == None
    assert linked_list_0.root.next.prev.val == None
    assert linked_list_0.root.next.next.val == 53
    assert linked_list_0.root.next.next.next.val == None
    assert linked_list_0.root.next.next.next.prev.val == 53
    
    linked_list_0.add_rule([97, 47])
    assert linked_list_0.root.next.val == 97
    assert linked_list_0.root.next.next.val == 47
    assert linked_list_0.root.next.next.next.val == 53
    
    linked_list_0.add_rule([53,29])
    assert linked_list_0.root.next.val == 97
    assert linked_list_0.root.next.next.val == 47
    assert linked_list_0.root.next.next.next.val == 53
    assert linked_list_0.root.next.next.next.next.val == 29

    linked_list_1: LinkedList = LinkedList(parsed_rules[0:4])
    assert linked_list_1 == [97, 13, 61, 47, 53]
    assert linked_list_1.can_add_rule([97, 75]) == True
    linked_list_1.add_rule([97,75])
    assert linked_list_1 == [97, 75, 13, 61, 47, 53]

    linked_list_2: LinkedList = LinkedList([parsed_rules[0]])
    assert linked_list_2 == [47, 53]
    assert linked_list_2.can_add_rule([97, 13]) == False
    assert linked_list_2.can_add_rule([97, 61]) == False
    assert linked_list_2.can_add_rule([97, 47]) == True
    linked_list_2.add_rule([97, 47])
    assert linked_list_2 == [97, 47, 53]
    assert linked_list_2.can_add_rule([75,29]) == False
    assert linked_list_2.can_add_rule([61,13]) == False
    assert linked_list_2.can_add_rule([75,53]) == True
    linked_list_2.add_rule([75, 53])
    assert linked_list_2 == [97, 47, 75, 53]
    assert linked_list_2.can_add_rule([29,13]) == False
    assert linked_list_2.can_add_rule([97,29]) == True
    linked_list_2.add_rule([97,29])
    assert linked_list_2 == [97, 29, 47, 75, 53]
    linked_list_2.add_rule([75, 29])
    assert linked_list_2 == [97, 75, 29, 47, 53]
    linked_list_2.add_rule([47, 29])
    assert linked_list_2 == [97, 75, 47, 29, 53]
    linked_list_2.add_rule([75, 47])
    assert linked_list_2 == [97, 75, 47, 29, 53]

    linked_list_full: LinkedList = LinkedList(parsed_rules.copy())
    unique_rules: list[int] = list(set([item for sublist in parsed_rules for item in sublist]))
    assert len(linked_list_full) == len(unique_rules)
    assert linked_list_full == [97, 75, 47, 61, 53, 29, 13]
