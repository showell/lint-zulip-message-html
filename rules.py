"""
We build a list of rules here to validate Zulip markdown
HMTL.  Note that the caller puts these rules into a
defaultdict of lists to make the checks more efficient,
so the order here isn't actually relevant.
"""

PARENT_RULES = [
    dict(tag="a", children=True),
    dict(tag="annotation", children=True),
    dict(tag="blockquote", children=True),
    dict(tag="code", children=True),
    dict(tag="del", children=True),
    dict(tag="div", children=True),
    dict(tag="em", children=True),
    dict(tag="p", children=True),
    dict(tag="pre", children=True),
    dict(tag="semantics", children=True),
    dict(tag="span", children=True),
    dict(tag="strong", children=True),
]

CHILD_RULES = [
    dict(tag="br"),
    dict(tag="hr"),
    dict(tag="img"),
    dict(tag="time"),
    dict(tag="video"),
]

HEADER_RULES = [
    dict(tag="h1"),
    dict(tag="h2"),
    dict(tag="h3"),
    dict(tag="h4"),
    dict(tag="h5"),
    dict(tag="h6"),
]

LIST_RULES = [
    dict(tag="li", children=True),
    dict(tag="ol", children=True),
    dict(tag="ul", children=True),
]

TABLE_RULES = [
    dict(tag="table", children=True),
    dict(tag="tbody", children=True),
    dict(tag="td", children=True),
    dict(tag="th", children=True),
    dict(tag="thead", children=True),
    dict(tag="tr", children=True),
]

MATH_PARENT_RULES = [
    dict(tag="math", children=True),
    dict(tag="mrow", children=True),
    dict(tag="msub", children=True),
    dict(tag="msup", children=True),
]

MATH_CHILD_RULES = [
    dict(tag="mi"),
    dict(tag="mn"),
    dict(tag="mo"),
    dict(tag="mtext"),
]

RULES = PARENT_RULES + CHILD_RULES + HEADER_RULES + LIST_RULES +  TABLE_RULES + MATH_PARENT_RULES + MATH_CHILD_RULES
