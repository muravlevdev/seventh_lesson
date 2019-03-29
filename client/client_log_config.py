import logging

def setup_log_config():
    file_handler = logging.FileHandler('client.log') 
    file_handler.setLevel(logging.DEBUG)
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            file_handler
        ]
    )
