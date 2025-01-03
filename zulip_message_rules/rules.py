from .span_checker import check_span_classes
from .style_checkers import check_span_style, check_svg_style, check_th_td_style
from html_validator.types import Node, ValidationConfig
from typing import Callable, Dict, Set

TAG_ATTR_MAP: Dict[str, Set[str]] = dict(
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

NO_ATTR_TAGS: Set[str] = {
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

for tag in NO_ATTR_TAGS:
    TAG_ATTR_MAP[tag] = set()

CUSTOM_TAG_HANLDERS: Dict[str, Callable[[Node], None]] = dict(
    span=check_span_classes,
)

CUSTOM_STYLE_CHECKERS: Dict[str, Callable[[Node, str], None]] = dict(
    span=check_span_style,
    svg=check_svg_style,
    th=check_th_td_style,
    td=check_th_td_style,
)

PARENT_CHILD_MAP: Dict[str, Set[str]] = dict(
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

LEAF_TAGS: Set[str] = {
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

TEXT_FRIENDLY_TAGS: Set[str] = {
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

for tag, attrs in TAG_ATTR_MAP.items():
    if "style" in attrs and tag not in CUSTOM_STYLE_CHECKERS:
        print(f"You need a style checker for {tag} tags")
        assert False

CLASS_VALUES: Dict[str, Set[str]] = dict(
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
    # note that <span> class values are checked in a custom handler
)

CONFIG: ValidationConfig = ValidationConfig(
    class_values=CLASS_VALUES,
    custom_style_checkers=CUSTOM_STYLE_CHECKERS,
    custom_tag_handlers=CUSTOM_TAG_HANLDERS,
    leaf_tags=LEAF_TAGS,
    parent_child_map=PARENT_CHILD_MAP,
    tag_attr_map=TAG_ATTR_MAP,
    text_friendly_tags=TEXT_FRIENDLY_TAGS,
)
