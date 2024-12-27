import json
import sys
from debug_helpers import BadZulipHtmlException
from lxml import html
from validator import validate
from test_data.backend_messages import BACKEND_MESSAGES
from test_data.frontend_messages import FRONTEND_MESSAGES


def validate_rows(rows):
    print(f"about to validate {len(rows)} rows")
    for row_html in rows:
        if row_html == "":
            continue
        ast = html.fromstring(row_html)
        try:
            validate(ast)
        except BadZulipHtmlException:
            print("FAIL")
            sys.exit()


json_payload = open("test_data/cases.json").read()
fixture_dicts = json.loads(json_payload)["regular_tests"]
fixture_rows = [fixture["expected_output"] for fixture in fixture_dicts]
validate_rows(fixture_rows)
validate_rows(BACKEND_MESSAGES)
validate_rows(FRONTEND_MESSAGES)
