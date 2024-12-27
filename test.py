import json
from lxml import html
from validator import validate, BrokenException

def validate_html(s):
    if s == "":
        return True
    ast = html.fromstring(s)
    if not validate(ast):
        print("BROKEN (full HTML follows):\n", s)
        return False
    return True

json_payload = open("cases.json").read()
for fixture in json.loads(json_payload)['regular_tests']:
    s = fixture["expected_output"]
    try:
        success = validate_html(s)
    except BrokenException:
        print ("FAIL")
        break
    if not success:
        print("FAIL")
        break
