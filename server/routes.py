import os
from functools import reduce
from importlib import __import__


def get_server_routes():
    print(os.listdir())
    return reduce(
        lambda routes, module: routes + getattr(module, 'routes', []),
        reduce(
            lambda modules, dir: modules + [__import__(f'{dir}.routes')],
            filter(
                lambda itm: os.path.isdir(itm) and itm != '__pycache__',
                os.listdir()
            ),
            []
        ),
        []
    )
