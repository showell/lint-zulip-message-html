from typing import Any


class IllegalHtmlException(Exception):
    pass


def ignore(s: str) -> None:
    pass


PrintMethod = Any


DEBUGGING_METHOD: PrintMethod = ignore


def debug_info(info: str) -> None:
    DEBUGGING_METHOD(info)


def set_debug_info_handler(*, method: PrintMethod) -> None:
    global DEBUGGING_METHOD
    DEBUGGING_METHOD = method
