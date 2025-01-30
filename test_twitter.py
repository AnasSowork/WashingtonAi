import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")


auth = tweepy.OAuth1UserHandler(
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_SECRET
)
api = tweepy.API(auth)

try:
    user = api.verify_credentials()
    print(f"✅ Twitter Bot Authenticated as {user.screen_name}")
except Exception as e:
    print("❌ Authentication failed:", e)
    exit()

def post_tweet():
    tweet_content = input("Enter the content of the tweet: ")
    try:
        api.update_status(tweet_content)
        print("✅ Tweet posted successfully!")
    except tweepy.errors.Forbidden as e:
        print(f"❌ Forbidden Error: {e}")
    except tweepy.errors.TweepyException as e:
        print(f"❌ Error posting tweet: {e}")

post_tweet()
