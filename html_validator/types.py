from dataclasses import dataclass
from typing import Callable, Dict, Set
from lxml.etree import _Element


Node = _Element


@dataclass
class ValidationConfig:
    class_values: Dict[str, Set[str]]
    custom_style_checkers: Dict[str, Callable[[Node, str], None]]
    custom_tag_handlers: Dict[str, Callable[[Node], None]]
    leaf_tags: Set[str]
    parent_child_map: Dict[str, Set[str]]
    tag_attr_map: Dict[str, Set[str]]
    text_friendly_tags: Set[str]


@dataclass
class IllegalHtmlException(Exception):
    node: Node
    message: str
