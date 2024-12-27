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
rows = [fixture["expected_output"] for fixture in json.loads(json_payload)['regular_tests']]
rows += json.loads(open("backend_messages.json").read())

for row_html in rows:
    try:
        success = validate_html(row_html)
    except BrokenException:
        print ("FAIL")
        break
    if not success:
        print("FAIL")
        break
