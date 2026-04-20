# configure log format
import logging
"""set up logger for banking application"""

def setup_logger():
    """create logger for banking application
    """

    logger = logging.getLogger('banking_logger')
    logger.setLevel(logging.DEBUG)
    """check if logger has handlers to avoid duplicate logs
    """

    if logger.hasHandlers():
        return logger
    """create file handler and set level to debug
    """

    file_handler = logging.FileHandler('banking.log')
    file_handler.setLevel(logging.DEBUG)

    """create formatter to specify log message format
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger