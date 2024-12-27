import json
import sys
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


def validate_rows(rows):
    print(f"about to validate {len(rows)} rows")
    for row_html in rows:
        try:
            success = validate_html(row_html)
        except BrokenException:
            print("FAIL")
            sys.exit()
        if not success:
            print("FAIL")
            sys.exit()


json_payload = open("cases.json").read()
fixture_rows = [
    fixture["expected_output"] for fixture in json.loads(json_payload)["regular_tests"]
]
validate_rows(fixture_rows)
validate_rows(json.loads(open("frontend_messages.json").read()))
validate_rows(json.loads(open("backend_messages.json").read()))
