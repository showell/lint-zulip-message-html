import sys
from html_validator.debug_helpers import IllegalHtmlException
from html_validator.validator import validate_html


def ensure_evil_messages_fail_checks(*, config, evil_payloads):
    for html in evil_payloads:
        try:
            validate_html(config=config, html=html)
        except IllegalHtmlException:
            continue
        print("FAIL: allowed evil message")
        print(html)
        sys.exit()


def validate_payloads(*, config, payloads):
    print(f"about to validate {len(payloads)} payloads")
    for html in payloads:
        if html == "":
            continue
        try:
            validate_html(config=config, html=html)
        except IllegalHtmlException:
            print("FAIL")
            sys.exit()
