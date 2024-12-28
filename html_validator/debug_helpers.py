from typing import Callable


class IllegalHtmlException(Exception):
    pass


def ignore(s):
    pass


DEBUGGING_METHOD = ignore


def debug_info(info: str) -> None:
    DEBUGGING_METHOD(info)


def set_debug_info_handler(*, method: Callable[[str], None]):
    global DEBUGGING_METHOD
    DEBUGGING_METHOD = method
