import json
import sys
from lxml import html
from validator import validate, BrokenException


def validate_rows(rows):
    print(f"about to validate {len(rows)} rows")
    for row_html in rows:
        if row_html == "":
            continue
        ast = html.fromstring(row_html)
        try:
            validate(ast)
        except BrokenException:
            print("FAIL")
            sys.exit()


json_payload = open("cases.json").read()
fixture_rows = [
    fixture["expected_output"] for fixture in json.loads(json_payload)["regular_tests"]
]
validate_rows(fixture_rows)
validate_rows(json.loads(open("frontend_messages.json").read()))
validate_rows(json.loads(open("backend_messages.json").read()))
