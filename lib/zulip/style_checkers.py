from ..generic.debug_helpers import debug_info, IllegalHtmlException
from ..generic.lxml_helpers import full_node_text
from ..generic.style_helpers import check_style


SPAN_VALID_KEYS = {
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


def check_span_style(node, style):
    if not check_style(style, SPAN_VALID_KEYS):
        debug_info(f"BAD style {style} FOR {node.tag}")
        debug_info(full_node_text(node))
        raise IllegalHtmlException


SVG_VALID_KEYS = {
    "width",
}


def check_svg_style(node, style):
    if not check_style(style, SVG_VALID_KEYS):
        debug_info(f"BAD style {style} FOR {node.tag}")
        debug_info(full_node_text(node))
        raise IllegalHtmlException


TH_TD_VALID_KEYS = {
    "text-align",
}


def check_th_td_style(node, style):
    if not check_style(style, TH_TD_VALID_KEYS):
        debug_info(f"BAD style {style} FOR {node.tag}")
        debug_info(full_node_text(node))
        raise IllegalHtmlException
