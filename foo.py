from lxml import html
from rules import RULES
import json

def check_rule(rule, node):
    return rule["tag"] == node.tag

def validate(node):
    for rule in RULES:
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
