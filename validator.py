from rules import RULES
from collections import defaultdict
from lxml import etree

RULES_DICT = defaultdict(list)


class BrokenException(Exception):
    pass


for rule in RULES:
    RULES_DICT[rule["tag"]].append(rule)


def node_text(node):
    return etree.tostring(node, encoding="unicode", method="html")


def validate_children(rule, node):
    children = node.getchildren()
    if children and not rule.get("children"):
        print("UNEXPECTED CHILDREN", node.tag, node_text(node))
        raise BrokenException

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
        print("UNSUPPORTED TAG", node.tag, node_text(node))
        raise BrokenException

    for rule in RULES_DICT[node.tag]:
        if validate_rule(rule, node):
            return True

    print("BROKEN TAG", node.tag, node_text(node))
    raise BrokenException
