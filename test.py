import json
import sys
from html_validator.debug_helpers import (
    IllegalHtmlException,
    turn_on_debugging,
)
from html_validator.validator import validate_html
from test_data.backend_messages import BACKEND_MESSAGES
from test_data.design_messages import DESIGN_MESSAGES
from test_data.feedback_messages import FEEDBACK_MESSAGES
from test_data.frontend_messages import FRONTEND_MESSAGES
from test_data.evil_messages import EVIL_MESSAGES
from lib.zulip.rules import CONFIG


def validate_rows(rows):
    print(f"about to validate {len(rows)} rows")
    for html in rows:
        if html == "":
            continue
        try:
            validate_html(config=CONFIG, html=html)
        except IllegalHtmlException:
            print("FAIL")
            sys.exit()


def ensure_evil_messages_fail_checks():
    for html in EVIL_MESSAGES:
        try:
            validate_html(config=CONFIG, html=html)
        except IllegalHtmlException:
            continue
        print("FAIL: allowed evil message")
        print(html)
        sys.exit()


ensure_evil_messages_fail_checks()

turn_on_debugging()

json_payload = open("test_data/cases.json").read()
fixture_dicts = json.loads(json_payload)["regular_tests"]
fixture_rows = [fixture["expected_output"] for fixture in fixture_dicts]
validate_rows(fixture_rows)
validate_rows(DESIGN_MESSAGES)
validate_rows(FEEDBACK_MESSAGES)
validate_rows(BACKEND_MESSAGES)
validate_rows(FRONTEND_MESSAGES)
