from .debug_helpers import debug_info, IllegalHtmlException
from .lxml_helpers import parse_html

from .lxml_helpers import (
    attr_keys,
    full_node_text,
    has_raw_text,
)


def validate_no_attr_tags(config, node, keys):
    if keys and node.tag in config.no_attr_tags:
        debug_info(f"TAG {node.tag} should never have attributes")
        debug_info(full_node_text(node))
        raise IllegalHtmlException


def validate_attr_tags(config, node, keys):
    if node.tag in config.attr_tags:
        for key in keys:
            if key not in config.attr_tags[node.tag]:
                debug_info(f"TAG {node.tag} has unknown attr {key}")
                debug_info(sorted(keys))
                debug_info(full_node_text(node))
                raise IllegalHtmlException


def validate_attr_classes(config, node, keys):
    if node.tag in config.class_values and "class" in keys:
        allowed_class_values = config.class_values[node.tag]
        node_class = node.attrib["class"]
        if node_class not in allowed_class_values:
            debug_info(f"TAG {node.tag} has unknown class {node_class}")
            debug_info(full_node_text(node))
            raise IllegalHtmlException


def validate_styles(config, node, keys):
    if "style" not in keys:
        return

    if node.tag in config.custom_style_checkers:
        style = node.attrib["style"]
        config.custom_style_checkers[node.tag](node, style)


def validate_attributes(config, node):
    keys = attr_keys(node)

    validate_no_attr_tags(config, node, keys)
    validate_attr_tags(config, node, keys)
    validate_attr_classes(config, node, keys)
    validate_styles(config, node, keys)


def validate_leaf_tag(config, node, children):
    if children and node.tag in config.leaf_tags:
        debug_info(f"UNEXPECTED CHILDREN for {node.tag}")
        debug_info(full_node_text(node))
        raise IllegalHtmlException


def validate_parent_child_restrictions(config, node, children):
    for c in children:
        if node.tag in config.parent_child_map:
            allowed_child_tags = config.parent_child_map[node.tag]
            if c.tag not in allowed_child_tags:
                debug_info(f"UNEXPECTED CHILD {c.tag} OF {node.tag}")
                debug_info(full_node_text(node))
                raise IllegalHtmlException


def validate_children(config, node):
    children = node.getchildren()
    validate_leaf_tag(config, node, children)
    validate_parent_child_restrictions(config, node, children)

    for c in children:
        validate_node(config, c)


def validate_text(config, node):
    if has_raw_text(node) and node.tag not in config.text_friendly_tags:
        debug_info(f"TAG {node.tag} unexpectedly has text")
        debug_info(full_node_text(node))
        raise IllegalHtmlException


def validate_tag_is_even_allowed(config, node):
    if node.tag not in config.all_tags:
        debug_info(f"UNSUPPORTED TAG {node.tag}")
        debug_info(full_node_text(node))
        raise IllegalHtmlException


def validate_custom_rules_for_tag(config, node):
    if node.tag in config.custom_tag_handlers:
        config.custom_tag_handlers[node.tag](node)


def validate_node(config, node):
    validate_tag_is_even_allowed(config, node)
    validate_attributes(config, node)
    validate_text(config, node)
    validate_children(config, node)
    validate_custom_rules_for_tag(config, node)


def validate_html(*, config, html):
    root = parse_html(html)
    validate_node(config, root)
