from .debug_helpers import debug_info, BadZulipHtmlException
from .lxml_helpers import parse_html

from .rules import (
    ALL_TAGS,
    ATTR_TAGS,
    CLASS_VALUES,
    LEAF_TAGS,
    NO_ATTR_TAGS,
    RESTRICTED_TAGS,
    TEXT_FRIENDLY_TAGS,
)

from .lxml_helpers import (
    attr_keys,
    full_node_text,
    has_raw_text,
)


def validate_no_attr_tags(node, keys):
    if keys and node.tag in NO_ATTR_TAGS:
        debug_info(f"TAG {node.tag} should never have attributes")
        debug_info(full_node_text(node))
        raise BadZulipHtmlException


def validate_attr_tags(node, keys):
    if node.tag in ATTR_TAGS:
        for key in keys:
            if key not in ATTR_TAGS[node.tag]:
                debug_info(f"TAG {node.tag} has unknown attr {key}")
                debug_info(sorted(keys))
                debug_info(full_node_text(node))
                raise BadZulipHtmlException


def validate_attr_classes(node, keys):
    if node.tag in CLASS_VALUES and "class" in keys:
        allowed_class_values = CLASS_VALUES[node.tag]
        node_class = node.attrib["class"]
        if node_class not in allowed_class_values:
            debug_info(f"TAG {node.tag} has unknown class {node_class}")
            debug_info(full_node_text(node))
            raise BadZulipHtmlException


def validate_attributes(node):
    keys = attr_keys(node)

    validate_no_attr_tags(node, keys)
    validate_attr_tags(node, keys)
    validate_attr_classes(node, keys)


def validate_leaf_tag(node, children):
    if children and node.tag in LEAF_TAGS:
        debug_info(f"UNEXPECTED CHILDREN for {node.tag}")
        debug_info(full_node_text(node))
        raise BadZulipHtmlException


def validate_parent_child_restrictions(node, children):
    for c in children:
        if node.tag in RESTRICTED_TAGS:
            if c.tag not in RESTRICTED_TAGS[node.tag]:
                debug_info(f"UNEXPECTED CHILD {c.tag} OF {node.tag}")
                debug_info(full_node_text(node))
                raise BadZulipHtmlException


def validate_children(node):
    children = node.getchildren()
    validate_leaf_tag(node, children)
    validate_parent_child_restrictions(node, children)

    for c in children:
        validate_node(c)


def validate_text(node):
    if has_raw_text(node) and node.tag not in TEXT_FRIENDLY_TAGS:
        debug_info(f"TAG {node.tag} unexpectedly has text")
        debug_info(full_node_text(node))
        raise BadZulipHtmlException


def validate_node(node):
    if node.tag not in ALL_TAGS:
        debug_info(f"UNSUPPORTED TAG {node.tag}")
        debug_info(full_node_text(node))
        raise BadZulipHtmlException

    validate_attributes(node)
    validate_text(node)
    validate_children(node)


def validate_html(message_html):
    root = parse_html(message_html)
    validate_node(root)
