import json
from html_validator.debug_helpers import set_debug_info_handler
from test_helpers import validate_payloads, ensure_evil_messages_fail_checks
from test_data.backend_messages import BACKEND_MESSAGES
from test_data.design_messages import DESIGN_MESSAGES
from test_data.feedback_messages import FEEDBACK_MESSAGES
from test_data.frontend_messages import FRONTEND_MESSAGES
from test_data.evil_messages import EVIL_MESSAGES
from zulip_message_rules.rules import CONFIG


def get_zulip_test_fixture_payloads():
    json_payload = open("test_data/cases.json").read()
    fixture_dicts = json.loads(json_payload)["regular_tests"]
    return [fixture["expected_output"] for fixture in fixture_dicts]


ensure_evil_messages_fail_checks(config=CONFIG, evil_payloads=EVIL_MESSAGES)

set_debug_info_handler(method=print)

validate_payloads(config=CONFIG, payloads=get_zulip_test_fixture_payloads())
validate_payloads(config=CONFIG, payloads=DESIGN_MESSAGES)
validate_payloads(config=CONFIG, payloads=FEEDBACK_MESSAGES)
validate_payloads(config=CONFIG, payloads=BACKEND_MESSAGES)
validate_payloads(config=CONFIG, payloads=FRONTEND_MESSAGES)

print("SUCCESS!")
