from rules import ALL_TAGS, RESTRICTED_TAGS, LEAF_TAGS
from lxml import etree


class BrokenException(Exception):
    pass


def node_text(node):
    return etree.tostring(node, encoding="unicode", method="html")


def validate_children(node):
    children = node.getchildren()

    if children and node.tag in LEAF_TAGS:
        print("UNEXPECTED CHILDREN", node.tag, node_text(node))
        raise BrokenException

    for c in children:
        if node.tag in RESTRICTED_TAGS:
            if c.tag not in RESTRICTED_TAGS[node.tag]:
                print(
                    f"UNEXPECTED CHILD {c.tag} OF {node.tag}", node.tag, node_text(node)
                )
                raise BrokenException

        if not validate(c):
            return False
    return True


def validate(node):
    if node.tag not in ALL_TAGS:
        print("UNSUPPORTED TAG", node.tag, node_text(node))
        raise BrokenException

    if not validate_children(node):
        print("BROKEN TAG", node.tag, node_text(node))
        raise BrokenException

    return True
