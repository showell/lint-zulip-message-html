from ..generic.debug_helpers import debug_info, BadZulipHtmlException
from ..generic.lxml_helpers import full_node_text


def check_style(style, valid_keys):
    """
    Example format:
        height:0.8889em;vertical-align:-0.1944em;

    We don't actually validate the values, just the keys.

    TODO: Add sanity checks for the actual values.
    """
    frags = [frag for frag in style.split(";") if frag != ""]

    for frag in frags:
        if ":" not in frag:
            return False
        css_key = frag.split(":")[0]
        if css_key not in valid_keys:
            return False

    return True


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
        raise BadZulipHtmlException


SVG_VALID_KEYS = {
    "width",
}


def check_svg_style(node, style):
    if not check_style(style, SVG_VALID_KEYS):
        debug_info(f"BAD style {style} FOR {node.tag}")
        debug_info(full_node_text(node))
        raise BadZulipHtmlException


TH_TD_VALID_KEYS = {
    "text-align",
}


def check_th_td_style(node, style):
    if not check_style(style, TH_TD_VALID_KEYS):
        debug_info(f"BAD style {style} FOR {node.tag}")
        debug_info(full_node_text(node))
        raise BadZulipHtmlException
