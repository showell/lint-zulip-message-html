from typing import Set


def check_style(style: str, valid_keys: Set[str]) -> bool:
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
