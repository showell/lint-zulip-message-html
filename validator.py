from rules import RULES

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
    for rule in RULES:
        if rule["tag"] == node.tag:
            if validate_rule(rule, node):
                return True

    print("UNKNOWN OR BROKEN TAG", node.tag, node.text)
    return False


