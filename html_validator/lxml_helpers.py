from lxml import html, etree
from typing import Set
from .types import Node


def parse_html(s: str) -> Node:
    return html.fromstring(s)


def attr_keys(node: Node) -> Set[str]:
    return set(str(s) for s in node.attrib.keys())


def full_node_text(node: Node) -> str:
    return etree.tostring(node, encoding="unicode", method="html")


def has_raw_text(node: Node) -> bool:
    # Check if the node itself has text content
    if node.text and node.text.strip():
        return True

    # Check if any child node has tail text
    for child in node.iterchildren():
        if child.tail and child.tail.strip():
            return True

    # If no text was found, return False
    return False
