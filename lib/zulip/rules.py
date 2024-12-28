from .span_checker import check_span_classes
from .style_checkers import check_span_style, check_svg_style, check_th_td_style
from ..generic.types import ValidationConfig

ALL_TAGS = {
    "a",
    "annotation",
    "blockquote",
    "body",
    "br",
    "code",
    "del",
    "div",
    "em",
    "h1",
    "h2",
    "h3",
    "h4",
    "h6",
    "hr",
    "html",
    "img",
    "li",
    "math",
    "mfrac",
    "mi",
    "mn",
    "mo",
    "mover",
    "mpadded",
    "mrow",
    "mstyle",
    "msub",
    "msubsup",
    "msup",
    "mtable",
    "mtext",
    "mtd",
    "mtr",
    "munderover",
    "ol",
    "p",
    "path",
    "pre",
    "semantics",
    "span",
    "strong",
    "svg",
    "table",
    "tbody",
    "td",
    "th",
    "thead",
    "time",
    "tr",
    "ul",
    "video",
}

CUSTOM_TAG_HANLDERS = dict(
    span=check_span_classes,
)

CUSTOM_STYLE_CHECKERS = dict(
    span=check_span_style,
    svg=check_svg_style,
    th=check_th_td_style,
    td=check_th_td_style,
)

PARENT_CHILD_MAP = dict(
    a={"code", "video", "img"},
    body={"div", "p"},
    code={"span"},
    html={"body"},
    ol={"li"},
    pre={"span", "code"},
    span={"span", "svg", "math"},
    svg={"path"},
    table={"thead", "tbody"},
    tbody={"tr"},
    thead={"tr"},
    tr={"th", "td"},
    ul={"li"},
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
    "path",
    "time",
    "video",
}

TEXT_FRIENDLY_TAGS = {
    "a",
    "annotation",
    "code",
    "del",
    "em",
    "h1",
    "h2",
    "h3",
    "h4",
    "h6",
    "li",
    "mi",
    "mn",
    "mo",
    "mtext",
    "p",
    "span",
    "strong",
    "td",
    "th",
    "time",
}

NO_ATTR_TAGS = {
    "blockquote",
    "body",
    "br",
    "code",
    "del",
    "em",
    "h1",
    "h2",
    "h3",
    "h4",
    "h6",
    "hr",
    "html",
    "li",
    "mfrac",
    "mn",
    "mover",
    "mrow",
    "msub",
    "msubsup",
    "msup",
    "mtext",
    "mtd",
    "mtr",
    "munderover",
    "p",
    "pre",
    "semantics",
    "strong",
    "table",
    "tbody",
    "thead",
    "tr",
    "ul",
}


ATTR_TAGS = dict(
    a={"class", "data-id", "data-stream-id", "href", "title"},
    annotation={"encoding"},
    div={"aria-hidden", "class", "data-code-language"},
    img={"alt", "class", "data-animated", "data-original-dimensions", "src", "title"},
    math={"display", "xmlns"},
    mi={"mathvariant"},
    mo={
        "fence",
        "lspace",
        "mathvariant",
        "maxsize",
        "minsize",
        "rspace",
        "separator",
        "stretchy",
    },
    mpadded={"lspace", "width", "voffset"},
    mstyle={"displaystyle", "scriptlevel"},
    mtable={"columnalign", "columnspacing", "rowspacing"},
    ol={"start"},
    path={"d"},
    span={
        "aria-hidden",
        "aria-label",
        "class",
        "data-user-group-id",
        "data-user-id",
        "role",
        "style",
        "title",
    },
    svg={"height", "preserveaspectratio", "style", "viewbox", "width", "xmlns"},
    td={"style"},
    th={"style"},
    time={"datetime"},
    video={"data-video-original-url", "preload", "src"},
)

for tag, attrs in ATTR_TAGS.items():
    if "style" in attrs and tag not in CUSTOM_STYLE_CHECKERS:
        print(f"You need a style checker for {tag} tags")
        assert False

# It's kind of annoying that I have these two data structures, but I
# like to call out the complicated cases.
assert (NO_ATTR_TAGS | set(ATTR_TAGS.keys())) == ALL_TAGS

# TODO: Find a way to validate span attributes. Unfortunately, there are a
#       zillion different span classes in Zulip messages due to things
#       like katex and emoji handling.
CLASS_VALUES = dict(
    a={"message-link", "stream", "stream-topic"},
    div={
        "codehilite",
        "inline-preview-twitter",
        "message_inline_image",
        "message_inline_image message_inline_video",
        "spoiler-block",
        "spoiler-content",
        "spoiler-header",
        "twitter-image",
        "twitter-tweet",
        "youtube-video message_inline_image",
    },
    img={"emoji", "twitter-avatar"},
)

CONFIG = ValidationConfig(
    all_tags=ALL_TAGS,
    attr_tags=ATTR_TAGS,
    class_values=CLASS_VALUES,
    custom_style_checkers=CUSTOM_STYLE_CHECKERS,
    custom_tag_handlers=CUSTOM_TAG_HANLDERS,
    leaf_tags=LEAF_TAGS,
    no_attr_tags=NO_ATTR_TAGS,
    parent_child_map=PARENT_CHILD_MAP,
    text_friendly_tags=TEXT_FRIENDLY_TAGS,
)
