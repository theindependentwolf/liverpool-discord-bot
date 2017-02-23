import praw
import config
import discord
import asyncio


def say_something():
    """
    Return post title of random post in 'noconext' subreddit
    """
    reddit = praw.Reddit(user_agent=config.my_user_agent,
                         client_id=config.my_client_id,
                         client_secret=config.my_client_secret)
    subreddit = reddit.subreddit("nocontext")
    
    while True:
        submission = subreddit.random()
        if submission.score >= 10:
            nocontext_message = submission.title    
            if nocontext_message.startswith('"') and nocontext_message.endswith('"'):
                nocontext_message = nocontext_message[1:-1]
            return nocontext_message




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
            return(str(advice))
