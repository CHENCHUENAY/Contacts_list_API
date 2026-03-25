import logging
import os

os.makedirs("results/logs", exist_ok=True)

logger = logging.getLogger("qa_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("results/logs/test_run.log", mode="a")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)