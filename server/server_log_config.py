import logging
from logging.handlers import TimedRotatingFileHandler

def setup_log_config():
    file_handler = TimedRotatingFileHandler('server.log', when="h", interval=24, backupCount=5) 
    file_handler.setLevel(logging.DEBUG)
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            file_handler
        ]
    )
