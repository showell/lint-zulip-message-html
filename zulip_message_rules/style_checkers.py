from html_validator.debug_helpers import debug_info, IllegalHtmlException
from html_validator.lxml_helpers import full_node_text
from html_validator.style_helpers import check_style
from html_validator.types import Node
from typing import Set


SPAN_VALID_KEYS: Set[str] = {
    "border-bottom-width",
    "bottom",
    "height",
    "margin-left",
    "margin-right",
    "min-width",
    "position",
    "top",
    "width",
    "vertical-align",
}


def check_span_style(node: Node, style: str):
    if not check_style(style, SPAN_VALID_KEYS):
        debug_info(f"BAD style {style} FOR {node.tag}")
        debug_info(full_node_text(node))
        raise IllegalHtmlException


SVG_VALID_KEYS: Set[str] = {
    "width",
}


def check_svg_style(node: Node, style: str):
    if not check_style(style, SVG_VALID_KEYS):
        debug_info(f"BAD style {style} FOR {node.tag}")
        debug_info(full_node_text(node))
        raise IllegalHtmlException


TH_TD_VALID_KEYS: Set[str] = {
    "text-align",
}


def check_th_td_style(node: Node, style: str):
    if not check_style(style, TH_TD_VALID_KEYS):
        debug_info(f"BAD style {style} FOR {node.tag}")
        debug_info(full_node_text(node))
        raise IllegalHtmlException
