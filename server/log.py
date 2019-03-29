from server_log_config import setup_log_config
import logging
import inspect

setup_log_config()

def log(func):
    def wrap(request, *args, **kwargs):
        logging.debug(f'Runnig function {func.__name__} from function {inspect.stack(0)[1][3]} with params: {request}')
        return func(request, *args, **kwargs)
    return wrap