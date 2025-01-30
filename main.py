from twitter_bot import post_tweet, reply_to_tweet, quote_tweet
from news_scraper import get_political_headlines
from satire_generator import generate_satire
from crypto_watchdog import check_crypto_scam

def run_bot():
    """Main function to run the AI satire bot."""

    headlines = get_political_headlines()
    
    if headlines:

        satire_tweet = generate_satire(f"Make fun of this news: {headlines[0]}")
        if satire_tweet:

            post_tweet(satire_tweet)
    
    scam_alert = check_crypto_scam("elonmusk")
    print(scam_alert)

    tweet_id = 'tweet_id_here'  
    reply_to_tweet(tweet_id, "Great work, Elon! 🚀")

if __name__ == "__main__":
    run_bot()
