class IllegalHtmlException(Exception):
    pass


DEBUGGING = False


def debug_info(info):
    if DEBUGGING:
        print(info)


def turn_on_debugging():
    global DEBUGGING
    DEBUGGING = True
