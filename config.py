import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    BEARER_TOKEN = os.getenv("BEARER_TOKEN")