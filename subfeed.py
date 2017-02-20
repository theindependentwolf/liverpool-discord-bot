import redis
import praw
import config
import time

def get_latest_post():
    """
    Get latest post from sub reddit. Redis DB is used to store older data in order to avoid duplicates. 
    This is used over the streaming api to avoid crashes from socket failures and use less system resources.
    """
    red = redis.Redis(host = 'localhost', db = config.subfeed_db)
    reddit = praw.Reddit(user_agent=config.my_user_agent,
                        client_id=config.my_client_id,
                        client_secret=config.my_client_secret) 
    subfeed_key = "sorted_lfc"
    unique_new_list = []
    subreddit = reddit.subreddit(config.subfeed_subreddit)
    for submission in subreddit.new(limit=config.subfeed_limit):
        current_time = int(time.time())
        present_in_db = red.zadd(subfeed_key, submission.id, current_time)
        if present_in_db == 1:
            submission_link = "https://www.reddit.com" + submission.permalink
            unique_new_list.append(submission_link)
    return unique_new_list




import twitter
import time



def get_latest_tweets():
    """
    Returns the latest tweets from the LFC Twitter Feed
    """
    tweet = twitter.Api(consumer_key=config.twitter_consumer_key, 
                    consumer_secret = config.twitter_consumer_secret, 
                    access_token_key = config.twitter_access_key, access_token_secret = config.twitter_access_secret)
    red = redis.Redis(host = 'localhost', db = config.subfeed_db)
    unique_new_list = []
    liverpool_tweet_list = tweet.GetUserTimeline(screen_name = config.twitter_screen_name, count = config.twitter_limit)
    twitter_key = "lfc_twitter"
    for lfctweet in liverpool_tweet_list:
        current_time = int(time.time()) 
        present_in_db = red.zadd(twitter_key, lfctweet.id, current_time)
        if present_in_db == 1:
            twitter_url = "https://www.twitter.com/" + config.twitter_screen_name + "/status/" + str(lfctweet.id)
            unique_new_list.append(twitter_url)
    return unique_new_list
