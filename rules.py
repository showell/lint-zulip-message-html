PARENT_RULES = [
    dict(tag="a", children=True),
    dict(tag="annotation", children=True),
    dict(tag="blockquote", children=True),
    dict(tag="code", children=True),
    dict(tag="del", children=True),
    dict(tag="div", children=True),
    dict(tag="em", children=True),
    dict(tag="li", children=True),
    dict(tag="ol", children=True),
    dict(tag="p", children=True),
    dict(tag="pre", children=True),
    dict(tag="semantics", children=True),
    dict(tag="span", children=True),
    dict(tag="strong", children=True),
    dict(tag="ul", children=True),
]

CHILD_RULES = [
    dict(tag="br"),
    dict(tag="h1"),
    dict(tag="h6"),
    dict(tag="img"),
    dict(tag="time"),
    dict(tag="video"),
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

RULES = PARENT_RULES + CHILD_RULES + TABLE_RULES + MATH_PARENT_RULES + MATH_CHILD_RULES
