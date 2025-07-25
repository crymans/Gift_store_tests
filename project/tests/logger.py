import logging

async def create_logger(name):
    logger_api = logging.getLogger(name)
    logger_api.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(f'{name}.log')

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M')

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger_api.addHandler(console_handler)
    logger_api.addHandler(file_handler)