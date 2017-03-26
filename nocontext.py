import praw
import config
import discord
import asyncio
import redis
import time

def say_something():
    """
    Return post title of random post in 'noconext' subreddit
    """
    reddit = praw.Reddit(user_agent=config.my_user_agent,
                         client_id=config.my_client_id,
                         client_secret=config.my_client_secret)
    red = redis.Redis(host = 'localhost', db = config.subfeed_db)
    filter_words = ['nigger','holocaust','jews','bomb','nazi']
    nocontext_key = "nocontext"
    subreddit = reddit.subreddit("nocontext")    
    while True:
        submission = subreddit.random()
        if submission.score >= 10 and not any(word in submission.title.lower().split() for word in filter_words):
            nocontext_message = submission.title    
            if nocontext_message.startswith('"') and nocontext_message.endswith('"'):
                nocontext_message = nocontext_message[1:-1]
            current_time = int(time.time())
            present_in_db = red.zadd(nocontext_key, submission.id, current_time)
            if present_in_db == 1:
                return nocontext_message
            else:
                pass




async def rlfc_new(bot):
    """
    Return new posts on /r/liverpoolfc
    """
    feed_channel = bot.get_channel(config.feed_channel)
    reddit = praw.Reddit(user_agent=config.my_user_agent,
                         client_id=config.my_client_id,
                         client_secret=config.my_client_secret)
    subreddit = reddit.subreddit("liverpoolfc")
    count = 0
    for submission in subreddit.stream.submissions():
        if count < 97:
            count += 1
            continue

        
        post_url = "https://www.reddit.com" + submission.permalink

        await bot.send_message(feed_channel, post_url)




         
       
def shower_birdie():
    """
    Return post title of random post in 'shower_thoughts' subreddit
    """
    reddit = praw.Reddit(user_agent=config.my_user_agent,
                         client_id=config.my_client_id,
                         client_secret=config.my_client_secret)
    subreddit = reddit.subreddit("showerthoughts")
    post = subreddit.random()
    return(str(post.title))    


def give_advice(advice_category):
    """
    Returns advice from shittylifeprotips
    """
    red = redis.Redis(host = 'localhost', db = config.subfeed_db)
    advice_key = "LPT"
    reddit = praw.Reddit(user_agent=config.my_user_agent,
                         client_id=config.my_client_id,
                         client_secret=config.my_client_secret)
    if advice_category == "need advice":
        subreddit = reddit.subreddit("ShittyLifeProTips")
    else:
        subreddit = reddit.subreddit("LifeProTips")
    
    while(True):
        submission = subreddit.random()
        if "reddit.com" in submission.url and submission.score >= 10:
            advice = submission.title
            advice = advice.replace("LPT:","")
            advice = advice.replace("lpt:","")
            advice = advice.strip()
            current_time = int(time.time())
            present_in_db = red.zadd(advice_key, submission.id, current_time)
            if present_in_db == 1:
                return(str(advice))
            else:
                pass
