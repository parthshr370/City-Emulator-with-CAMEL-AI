import logging


def get_logger(name: str):
    logger = logging.getLogger(name)
    if not logger.handlers:  # Prevents duplicate handlers
        logger.setLevel(logging.DEBUG)  # Set the logger level to DEBUG
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)  # Set the handler level to INFO
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )  # Define the log message format
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger
