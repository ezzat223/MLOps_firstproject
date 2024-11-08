import logging
import os
from datetime import datetime

# Define log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define log directory and create if it doesn't exist
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

# Complete log file path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    level=logging.INFO, 
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(filename)s:%(lineno)d - %(levelname)s - %(message)s"
)

# For testing purposes, run this file and log a message
if __name__ == "__main__":
    logging.info("Testing log configuration.")
    # [2024-11-07 22:28:36,281] app_logging.py:24 - INFO - Testing log configuration.