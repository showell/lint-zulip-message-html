PARENT_RULES = [
    dict(tag="a", children=True),
    dict(tag="blockquote", children=True),
    dict(tag="del", children=True),
    dict(tag="div", children=True),
    dict(tag="em", children=True),
    dict(tag="li", children=True),
    dict(tag="ol", children=True),
    dict(tag="math", children=True),
    dict(tag="mrow", children=True),
    dict(tag="msub", children=True),
    dict(tag="msup", children=True),
    dict(tag="p", children=True),
    dict(tag="pre", children=True),
    dict(tag="semantics", children=True),
    dict(tag="span", children=True),
    dict(tag="strong", children=True),
    dict(tag="ul", children=True),
]

CHILD_RULES = [
    dict(tag="br"),
    dict(tag="code"),
    dict(tag="h1"),
    dict(tag="h6"),
    dict(tag="img"),
    dict(tag="mi"),
    dict(tag="mn"),
    dict(tag="mo"),
    dict(tag="mtext"),
    dict(tag="time"),
    dict(tag="video"),
]

RULES = PARENT_RULES + CHILD_RULES
