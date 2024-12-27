from rules import ALL_TAGS, RESTRICTED_TAGS, LEAF_TAGS, TEXT_FRIENDLY_TAGS
from lxml import etree


class BrokenException(Exception):
    pass


def full_node_text(node):
    return etree.tostring(node, encoding="unicode", method="html")


def has_raw_text(node):
    # Check if the node itself has text content
    if node.text and node.text.strip():
        return True

    # Check if any child node has tail text
    for child in node.iterchildren():
        if child.tail and child.tail.strip():
            return True

    # If no text was found, return False
    return False


def validate_children(node):
    children = node.getchildren()

    if children and node.tag in LEAF_TAGS:
        print("UNEXPECTED CHILDREN", node.tag, full_node_text(node))
        raise BrokenException

    for c in children:
        if node.tag in RESTRICTED_TAGS:
            if c.tag not in RESTRICTED_TAGS[node.tag]:
                print(
                    f"UNEXPECTED CHILD {c.tag} OF {node.tag}",
                    node.tag,
                    full_node_text(node),
                )
                raise BrokenException

        if not validate(c):
            return False
    return True


def validate(node):
    if has_raw_text(node) and node.tag not in TEXT_FRIENDLY_TAGS:
        print(f"TAG {node.tag} unexpectedly has text")
        print(full_node_text(node))
        raise BrokenException

    if node.tag not in ALL_TAGS:
        print("UNSUPPORTED TAG", node.tag, full_node_text(node))
        raise BrokenException

    if not validate_children(node):
        print("BROKEN TAG", node.tag, full_node_text(node))
        raise BrokenException

    return True
