from lxml import html
from rules import RULES
import json

def validate(node):
    for rule in RULES:
        if rule["tag"] == node.tag:
            break
    else:
        print("BROKEN", node.tag, node.text)
        return False
    children = node.getchildren()
    if children and not rule.get("children"):
        print("BROKEN RULE", node.tag, node.text)
        return False
    for c in children:
        if not validate(c):
            return False
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
