from rules import RULES
from collections import defaultdict

RULES_DICT = defaultdict(list)

for rule in RULES:
    RULES_DICT[rule["tag"]].append(rule)

def validate_children(rule, node):
    children = node.getchildren()
    if children and not rule.get("children"):
        print("UNEXPECTED CHILDREN", node.tag, node.text)
        return False

    for c in children:
        if not validate(c):
            return False
    return True

def validate_rule(rule, node):
    if not validate_children(rule, node):
        return False
    return True

def validate(node):
    if node.tag not in RULES_DICT:
        print("UNSUPPORTED TAG", node.tag, node.text)
        return False

    for rule in RULES_DICT[node.tag]:
        if validate_rule(rule, node):
            return True

    print("BROKEN TAG", node.tag, node.text)
    return False


