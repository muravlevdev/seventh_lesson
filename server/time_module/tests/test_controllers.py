from time_module.controllers import (
    get_time
)

from datetime import datetime


def test_get_time():
    assert get_time('') == datetime.now().strftime('%d-%m-%yT%H:%M:%S')