from .debug_helpers import debug_info, BadZulipHtmlException
from .lxml_helpers import full_node_text


def check_style(style, valid_keys):
    """
    Example format:
        height:0.8889em;vertical-align:-0.1944em;
    """
    if not style.endswith(";"):
        return False

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
