from html_validator.style_helpers import check_style
from html_validator.types import IllegalHtmlException, Node
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


def check_span_style(node: Node, style: str) -> None:
    if not check_style(style, SPAN_VALID_KEYS):
        raise IllegalHtmlException(
            node=node, message=f"BAD style {style} FOR {node.tag}"
        )


SVG_VALID_KEYS: Set[str] = {
    "width",
}


def check_svg_style(node: Node, style: str) -> None:
    if not check_style(style, SVG_VALID_KEYS):
        raise IllegalHtmlException(
            node=node, message=f"BAD style {style} FOR {node.tag}"
        )


TH_TD_VALID_KEYS: Set[str] = {
    "text-align",
}


def check_th_td_style(node: Node, style: str) -> None:
    if not check_style(style, TH_TD_VALID_KEYS):
        raise IllegalHtmlException(
            node=node, message=f"BAD style {style} FOR {node.tag}"
        )
