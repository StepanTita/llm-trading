import logging
import os.path
import traceback

from utils import grey, cyan, yellow, red, bold


class CustomTerminalFormatter(logging.Formatter):
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    reset = '\033[0m'

    FORMATS = {
        logging.DEBUG: grey(format) + reset,
        logging.INFO: cyan(format) + reset,
        logging.WARNING: yellow(format) + reset,
        logging.ERROR: red(format) + reset,
        logging.CRITICAL: bold(red(format)) + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class CustomFileFormatter(logging.Formatter):
    def format(self, record):
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        return formatter.format(record)


class SelectiveLogger:
    def __init__(self, terminal_logger, file_logger):
        self.term = terminal_logger
        self.file = file_logger

    def info(self, msg='', terminal=True):
        if terminal:
            self.term.info(msg)
        self.file.info(msg)

    def debug(self, msg='', terminal=True):
        if terminal:
            self.term.debug(msg)
        self.file.debug(msg)

    def warn(self, msg='', terminal=True):
        if terminal:
            self.term.warn(msg)
        self.file.warn(msg)

    def error(self, msg='', terminal=True):
        if terminal:
            self.term.error(msg)
        self.file.error(msg)

    def critical(self, msg='', terminal=True):
        if terminal:
            self.term.critical(msg)
        self.file.critical(msg)
        
sh = logging.StreamHandler()
sh.setFormatter(CustomTerminalFormatter())
        
def get_logger(log_path, log_file, log_name='default'):
    global sh
    
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    term = logging.getLogger(log_name).getChild('terminal')
    file = logging.getLogger(log_name).getChild('file')

    fh = logging.FileHandler(f'{log_path}/{log_file}.log')
    fh.setFormatter(CustomFileFormatter())

    # link handler to logger
    term.addHandler(sh)
    file.addHandler(fh)

    # Set logging level to the logger
    term.setLevel(logging.DEBUG)
    file.setLevel(logging.DEBUG)

    return SelectiveLogger(term, file)

