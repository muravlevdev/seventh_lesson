from .controllers import (
    get_upper_text, get_lower_text
)


routes = [
    {'action': 'upper_text', 'controller': get_upper_text},
    {'action': 'lower_text', 'controller': get_lower_text},
]