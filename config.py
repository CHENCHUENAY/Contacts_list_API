import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://thinking-tester-contact-list.herokuapp.com"

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")