from log import log

@log
def get_upper_text(data):
    return data.upper()

@log
def get_lower_text(data):
    return data.lower()
