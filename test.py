import json
from lxml import html
from validator import validate

json_payload = open("cases.json").read()
for fixture in json.loads(json_payload)['regular_tests']:
    s = fixture["expected_output"]
    if s == "":
        continue
    ast = html.fromstring(s)
    if not validate(ast):
        print("BROKEN BIG", s)
        break
