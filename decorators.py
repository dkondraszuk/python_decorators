import logging
import time
from functools import wraps

from my_logger import log


def step_logger(step_function):
    @wraps(step_function)
    def wrapper(*args, **kwargs):
        name = step_function.__name__
        log(logging.INFO, "***** Started {}: '{}' *****".format('test' if 'test' in name else 'step', name))
        result = step_function(*args, **kwargs)
        log(logging.INFO, "***** Finished {}: '{}' *****".format('test' if 'test' in name else 'step', name))
        return result
    return wrapper


def measure_time(step_function):
    @wraps(step_function)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = step_function(*args, **kwargs)
        t_stop = time.time()
        log(logging.INFO, '--- Execution time of "{}" function: {:.3f} seconds ---'.format(step_function.__name__,
                                                                                           t_stop - t_start))
        return result
    return wrapper


def decorate_all_steps(decorator):
    def decorate(cls):
        for fn_name, fn in cls.__dict__.iteritems():
            if not fn_name.startswith('_'):
                if callable(fn):
                    setattr(cls, fn_name, decorator(fn))
        return cls
    return decorate
