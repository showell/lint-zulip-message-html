from .debug_helpers import debug_info, IllegalHtmlException
from .lxml_helpers import parse_html
from .types import Node, ValidationConfig
from typing import List, Set
from .lxml_helpers import (
    attr_keys,
    full_node_text,
    has_raw_text,
)


def validate_no_attr_tags(config: ValidationConfig, node: Node, keys: Set[str]) -> None:
    if keys and node.tag in config.no_attr_tags:
        debug_info(f"TAG {node.tag} should never have attributes")
        debug_info(full_node_text(node))
        raise IllegalHtmlException


def validate_attr_tags(config: ValidationConfig, node: Node, keys: Set[str]) -> None:
    if node.tag in config.attr_tags:
        for key in keys:
            if key not in config.attr_tags[node.tag]:
                debug_info(f"TAG {node.tag} has unknown attr {key}")
                debug_info(str(sorted(keys)))
                debug_info(full_node_text(node))
                raise IllegalHtmlException


def validate_attr_classes(config: ValidationConfig, node: Node, keys: Set[str]) -> None:
    if node.tag in config.class_values and "class" in keys:
        allowed_class_values = config.class_values[node.tag]
        node_class = str(node.attrib["class"])
        if node_class not in allowed_class_values:
            debug_info(f"TAG {node.tag} has unknown class {node_class}")
            debug_info(full_node_text(node))
            raise IllegalHtmlException


def validate_styles(config: ValidationConfig, node: Node, keys: Set[str]) -> None:
    if "style" not in keys:
        return

    if node.tag in config.custom_style_checkers:
        style = str(node.attrib["style"])
        config.custom_style_checkers[node.tag](node, style)


def validate_attributes(config: ValidationConfig, node: Node) -> None:
    keys = attr_keys(node)

    validate_no_attr_tags(config, node, keys)
    validate_attr_tags(config, node, keys)
    validate_attr_classes(config, node, keys)
    validate_styles(config, node, keys)


def validate_leaf_tag(
    config: ValidationConfig, node: Node, children: List[Node]
) -> None:
    if children and node.tag in config.leaf_tags:
        debug_info(f"UNEXPECTED CHILDREN for {node.tag}")
        debug_info(full_node_text(node))
        raise IllegalHtmlException


def validate_parent_child_restrictions(
    config: ValidationConfig, node: Node, children: List[Node]
) -> None:
    for c in children:
        if node.tag in config.parent_child_map:
            allowed_child_tags = config.parent_child_map[node.tag]
            if c.tag not in allowed_child_tags:
                debug_info(f"UNEXPECTED CHILD {c.tag} OF {node.tag}")
                debug_info(full_node_text(node))
                raise IllegalHtmlException


def validate_children(config: ValidationConfig, node: Node) -> None:
    children = list(node.iterchildren())
    validate_leaf_tag(config, node, children)
    validate_parent_child_restrictions(config, node, children)

    for c in children:
        validate_node(config, c)


def validate_text(config: ValidationConfig, node: Node) -> None:
    if has_raw_text(node) and node.tag not in config.text_friendly_tags:
        debug_info(f"TAG {node.tag} unexpectedly has text")
        debug_info(full_node_text(node))
        raise IllegalHtmlException


def validate_tag_is_even_allowed(config: ValidationConfig, node: Node) -> None:
    if node.tag not in config.all_tags:
        debug_info(f"UNSUPPORTED TAG {node.tag}")
        debug_info(full_node_text(node))
        raise IllegalHtmlException


def validate_custom_rules_for_tag(config: ValidationConfig, node: Node) -> None:
    if node.tag in config.custom_tag_handlers:
        config.custom_tag_handlers[node.tag](node)


def validate_node(config: ValidationConfig, node: Node) -> None:
    validate_tag_is_even_allowed(config, node)
    validate_attributes(config, node)
    validate_text(config, node)
    validate_children(config, node)
    validate_custom_rules_for_tag(config, node)


def validate_html(*, config: ValidationConfig, html: str) -> None:
    root = parse_html(html)
    validate_node(config, root)
