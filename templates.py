import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')


# logging.info("Welcome to this project")

list_of_files = [
    "tradingbot/__init__.py",
    "tradingbot/helper.py",
    "tradingbot/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/test.ipynb",
    "app.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the files {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")

    