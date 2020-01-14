import logging

from colorlog import ColoredFormatter

LOG_PATH = 'tmp.log'
LOG_TO_FILE = True
CONSOLE_FORMAT = '  %(log_color)s%(levelname)-8s%(reset)s %(log_color)s| %(log_color)s%(message)s%(reset)s'
FILE_FORMAT = '%(asctime)s | %(levelname)-8s | %(message)s'
DATE_FORMAT = '%d/%m/%Y %H:%M:%S'
LOG_COLORS = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}

logging.raiseExceptions = True

# create custom logger instance:
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_formatter = ColoredFormatter(fmt=CONSOLE_FORMAT, log_colors=LOG_COLORS)
console_handler = logging.StreamHandler()
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# create file handler, formatter and add to logger instance if specified:
if LOG_TO_FILE:
    file_formatter = logging.Formatter(fmt=FILE_FORMAT, datefmt=DATE_FORMAT)
    file_handler = logging.FileHandler(filename=LOG_PATH, mode='w', encoding='utf-8')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

# log - this is the method we are using:
log = logger.log

if __name__ == '__main__':
    log(logging.DEBUG, "A quirky message only developers care about")
    log(logging.INFO, "Curious users might want to know this")
    log(logging.WARNING, "Something is wrong and any user should be informed")
    log(logging.ERROR, "Serious stuff, this is red for a reason")
    log(logging.CRITICAL, "OH NO everything is on fire")
