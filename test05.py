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
    assert linked_list_0.root.next.next.val == 53

    linked_list_0.add_rule([97, 47])
    assert linked_list_0.root.next.val == 97
    assert linked_list_0.root.next.next.val == 47
    assert linked_list_0.root.next.next.next.val == 53

    # linked_list_1 = LinkedList(parsed_rules[0:4])
    # rule_0 = linked_list.root
    #
    # assert rule_0.val == None
    # assert rule_0.next.val == 97
    # assert rule_0.next.next.val == 13
    # assert rule_0.next.next.next.val == 61
    # assert rule_0.next.next.next.next.val == 47
    # assert rule_0.next.next.next.next.next.val == 53
