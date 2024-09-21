import os

from dotenv import load_dotenv

load_dotenv("env.txt")
URL = os.getenv("URL", "")
