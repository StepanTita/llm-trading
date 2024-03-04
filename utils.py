import time


def style(s, style):
    return style + s + '\033[0m'


def grey(s):
    return style(s, '\033[90m')


def green(s):
    return style(s, '\033[92m')


def blue(s):
    return style(s, '\033[94m')


def yellow(s):
    return style(s, '\033[93m')


def red(s):
    return style(s, '\033[91m')


def pink(s):
    return style(s, '\033[95m')


def cyan(s):
    return style(s, '\033[36m')


def bold(s):
    return style(s, '\033[1m')


def underline(s):
    return style(s, '\033[4m')


def current_time():
    return int(time.time() * 1000)


def free_resources_deco(func):
    import torch
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        finally:
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
    return wrapper