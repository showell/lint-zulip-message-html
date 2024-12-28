from lxml import html, etree


def parse_html(s):
    node = html.fromstring(s)
    # work around the annoyting fact that some Zulip
    # messagea around enclosed in body/html tags
    # introduces <html> tags around our html
    if node.tag == "html":
        node = node.getchildren()[0]
        assert node.tag == "body"
        node = node.getchildren()[0]

    return node


def attr_keys(node):
    return tuple(sorted(node.attrib.keys()))


def full_node_text(node):
    return etree.tostring(node, encoding="unicode", method="html")


def has_raw_text(node):
    # Check if the node itself has text content
    if node.text and node.text.strip():
        return True

    # Check if any child node has tail text
    for child in node.iterchildren():
        if child.tail and child.tail.strip():
            return True

    # If no text was found, return False
    return False
