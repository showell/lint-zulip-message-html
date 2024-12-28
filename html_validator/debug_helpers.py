class IllegalHtmlException(Exception):
    pass


def ignore(s):
    pass


DEBUGGING_METHOD = ignore


def debug_info(info):
    DEBUGGING_METHOD(info)


def set_debug_info_handler(*, method):
    global DEBUGGING_METHOD
    DEBUGGING_METHOD = method
