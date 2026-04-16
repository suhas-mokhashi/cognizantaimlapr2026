#configure log format
import logging
"""set up logger for healthcare application"""

def setup_logger():
    """create logger for healthcare application
    """

    logger=logging.getLogger('healthcare_logger')
    logger.setLevel(logging.DEBUG)
    """check if logger has handlers to avoid duplicate logs
    """

    if logger.hasHandlers():
        return logger
    """create file handler and set level to debug
    """

    file_handler=logging.FileHandler('healthcare.log')
    logger.setLevel(logging.DEBUG)
    
    """create formatter to specify log message format
    """
    formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger