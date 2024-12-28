import sys
from html_validator.debug_helpers import IllegalHtmlException
from html_validator.validator import validate_html

def ensure_evil_messages_fail_checks(*, config, evil_rows):
    for html in evil_rows:
        try:
            validate_html(config=config, html=html)
        except IllegalHtmlException:
            continue
        print("FAIL: allowed evil message")
        print(html)
        sys.exit()


def validate_rows(*, config, rows):
    print(f"about to validate {len(rows)} rows")
    for html in rows:
        if html == "":
            continue
        try:
            validate_html(config=config, html=html)
        except IllegalHtmlException:
            print("FAIL")
            sys.exit()
