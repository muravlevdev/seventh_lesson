from datetime import datetime
from log import log

@log
def get_time(data):
    date = datetime.now()
    return date.strftime('%d-%m-%yT%H:%M:%S')
