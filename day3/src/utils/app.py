import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from configuration.logger_conf import setup_logger

"""entry point for the application
"""
logger = setup_logger()

def run():
    """test logger
    """
    logger.info("app run")

"""handle entry point
"""
if __name__ == "__main__":
    run()


