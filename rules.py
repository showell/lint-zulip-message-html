"""
We build a list of rules here to validate Zulip markdown
HMTL.  Note that the caller puts these rules into a
defaultdict of lists to make the checks more efficient,
so the order here isn't actually relevant.
"""

PARENT_RULES = [
    dict(tag="a"),
    dict(tag="annotation"),
    dict(tag="blockquote"),
    dict(tag="code"),
    dict(tag="del"),
    dict(tag="div"),
    dict(tag="em"),
    dict(tag="p"),
    dict(tag="pre"),
    dict(tag="semantics"),
    dict(tag="span"),
    dict(tag="strong"),
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
    dict(tag="li"),
    dict(tag="ol"),
    dict(tag="ul"),
]

TABLE_RULES = [
    dict(tag="table"),
    dict(tag="tbody"),
    dict(tag="td"),
    dict(tag="th"),
    dict(tag="thead"),
    dict(tag="tr"),
]

MATH_PARENT_RULES = [
    dict(tag="math"),
    dict(tag="mfrac"),
    dict(tag="mrow"),
    dict(tag="msub"),
    dict(tag="msubsup"),
    dict(tag="msup"),
]

MATH_CHILD_RULES = [
    dict(tag="mi"),
    dict(tag="mn"),
    dict(tag="mo"),
    dict(tag="mtext"),
]

RULES = (
    PARENT_RULES
    + CHILD_RULES
    + HEADER_RULES
    + LIST_RULES
    + TABLE_RULES
    + MATH_PARENT_RULES
    + MATH_CHILD_RULES
)

"""
The following list mined from ~250,000 real-world Zulip messages,
It's imperfect:
    * it omits tags like "p" that can include almost any other tag
    * it may be over-restrictive on other things
"""
RESTRICTED_TAGS = dict(
    a={'code', 'video', 'img'},
    code={'span'},
    em={'code', 'a'},
    math={'semantics'},
    mfrac={'mrow', 'mi'},
    mrow={'mo', 'mtext', 'mi', 'msubsup', 'mfrac', 'mn', 'msub', 'msup'},
    msub={'mi'},
    msubsup={'mo', 'mn', 'msup'},
    msup={'mo', 'mn', 'mi'},
    ol={'li'},
    pre={'span', 'code'},
    semantics={'mrow', 'annotation'},
    span={'span', 'math'},
    strong={'span', 'code', 'em', 'a'},
    table={'thead', 'tbody'},
    tbody={'tr'},
    thead={'tr'},
    tr={'th', 'td'},
    ul={'li'},
)

LEAF_TAGS = {
    "annotation",
    "br",
    "hr",
    "img",
    "mi",
    "mn",
    "mo",
    "mtext",
    "td",
    "th",
    "time",
    "video",
}
