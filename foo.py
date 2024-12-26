from lxml import html
import json

# Sample HTML string
html_string = """
"""

def check_rule(rule, node):
    return rule["tag"] == node.tag

def validate(node):
    print(node.tag)
    rules = [
        dict(tag="a"),
        dict(tag="blockquote"),
        dict(tag="br"),
        dict(tag="code"),
        dict(tag="del"),
        dict(tag="div"),
        dict(tag="em"),
        dict(tag="h1"),
        dict(tag="h6"),
        dict(tag="img"),
        dict(tag="li"),
        dict(tag="ol"),
        dict(tag="math"),
        dict(tag="mi"),
        dict(tag="mn"),
        dict(tag="mo"),
        dict(tag="mrow"),
        dict(tag="msub"),
        dict(tag="msup"),
        dict(tag="mtext"),
        dict(tag="p"),
        dict(tag="pre"),
        dict(tag="semantics"),
        dict(tag="span"),
        dict(tag="strong"),
        dict(tag="time"),
        dict(tag="ul"),
        dict(tag="video"),
    ]
    for rule in rules:
        if check_rule(rule, node):
            break
    else:
        print("BROKEN", node.tag, node.text)
        return False
    for c in node.getchildren():
        return validate(c)
    return True

# Parse the HTML string
# root = html.fromstring(html_string)

json_payload = open("cases.json").read()
for fixture in json.loads(json_payload)['regular_tests']:
    s = fixture["expected_output"]
    if s == "":
        continue
    ast = html.fromstring(s)
    if not validate(ast):
        print("BROKEN BIG", s)
        break
