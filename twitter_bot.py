import tweepy
from config import Config

# Authenticate Twitter API
auth = tweepy.OAuthHandler(Config.TWITTER_API_KEY, Config.TWITTER_API_SECRET)
auth.set_access_token(Config.TWITTER_ACCESS_TOKEN, Config.TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

def post_tweet(content):
    """Posts a tweet"""
    try:
        api.update_status(content)
        print("Tweet posted successfully!")
    except Exception as e:
        print("Error posting tweet:", e)

def reply_to_tweet(tweet_id, content):
    """Replies to a tweet"""
    try:
        api.update_status(status=content, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
        print("Reply posted successfully!")
    except Exception as e:
        print("Error replying to tweet:", e)
