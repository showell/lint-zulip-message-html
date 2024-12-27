from rules import (
    ALL_TAGS,
    ATTR_TAGS,
    CLASS_VALUES,
    LEAF_TAGS,
    NO_ATTR_TAGS,
    RESTRICTED_TAGS,
    TEXT_FRIENDLY_TAGS,
)
from lxml import etree


class BrokenException(Exception):
    pass


def attr_keys(node):
    return tuple(sorted(node.attrib.keys()))


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


def validate_attributes(node):
    keys = attr_keys(node)
    if keys and node.tag in NO_ATTR_TAGS:
        print(f"TAG {node.tag} should never have attributes")
        print(full_node_text(node))
        raise BrokenException

    if node.tag in ATTR_TAGS:
        for key in keys:
            if key not in ATTR_TAGS[node.tag]:
                print(f"TAG {node.tag} has unknown attr {key}")
                print(full_node_text(node))
                raise BrokenException

    if node.tag in CLASS_VALUES and "class" in keys:
        allowed_class_values = CLASS_VALUES[node.tag]
        node_class = node.attrib["class"]
        if node_class not in allowed_class_values:
            print(f"TAG {node.tag} has unknown class {node_class}")
            print(full_node_text(node))
            raise BrokenException


def validate_children(node):
    children = node.getchildren()

    if children and node.tag in LEAF_TAGS:
        print(f"UNEXPECTED CHILDREN for {node.tag}")
        print(full_node_text(node))
        raise BrokenException

    for c in children:
        if node.tag in RESTRICTED_TAGS:
            if c.tag not in RESTRICTED_TAGS[node.tag]:
                print(f"UNEXPECTED CHILD {c.tag} OF {node.tag}")
                print(full_node_text(node))
                raise BrokenException

        validate(c)


def validate(node):
    validate_attributes(node)

    if has_raw_text(node) and node.tag not in TEXT_FRIENDLY_TAGS:
        print(f"TAG {node.tag} unexpectedly has text")
        print(full_node_text(node))
        raise BrokenException

    if node.tag not in ALL_TAGS:
        print(f"UNSUPPORTED TAG {node.tag}")
        print(full_node_text(node))
        raise BrokenException

    validate_children(node)
