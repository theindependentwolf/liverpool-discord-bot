import discord
from discord.ext import commands
import random
from random import randint
import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import functions
import config
import datetime
import dateutil.relativedelta as relativetd
import nocontext as reddit
import asyncio
import praw
import subfeed
import re

description = ''' Birdie-G, a red avian bot. '''

bot = commands.Bot(command_prefix='!', description = description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    """
    Processes incoming message to do various fun stuff
    """
    response = functions.processMessage(message, bot)
    if response:
        await bot.send_message(message.channel, response)
    await bot.process_commands(message)



async def no_context_general():
    """
    Send a message from /r/nocontext
    """
    await bot.wait_until_ready()
    talk_interval = 25000
    nocontext_channel = discord.Object(id=config.nocontext_channel_id)
    while not bot.is_closed:
        nocontext_message = reddit.say_something()
        await asyncio.sleep(talk_interval)
        await bot.send_message(nocontext_channel, nocontext_message)


async def subredditfeed():
    """
    Post new posts from subreddit to the chat. Updates happens every few minutes. 
    """
    await bot.wait_until_ready()
    subfeed_channel = discord.Object(id=config.subfeed_channel_id)
    while not bot.is_closed:
        new_posts = subfeed.get_latest_post()
        if new_posts:
            for post in new_posts[::-1]:
                await bot.send_message(subfeed_channel, post)
        else:
            pass
            
        await asyncio.sleep(config.subfeed_update_interval)



async def twitterfeed():
    """
    Post new posts from LFC Twitter to the chat. Updates happens every few minutes. 
    """
    await bot.wait_until_ready()
    twitter_channel = discord.Object(id=config.twitter_channel_id)
    while not bot.is_closed:
        new_posts = subfeed.get_latest_tweets()
        if new_posts:
            for post in new_posts[::-1]:
                await bot.send_message(twitter_channel, post)
        else:
            pass

        await asyncio.sleep(config.twitter_update_interval)



@bot.command()
async def predict(team1: str, team2: str):
    """
    !predict Liverpool Spurs
    """
    if team1 and team2:
        result = functions.predict(team1, team2)
    else:
        result = "Missing arguments. Please mention two teams."
    embed = discord.Embed(description=result, colour=discord.Colour(0xcc0000))
    await bot.say(embed=embed)


@bot.command()
async def gifs(gifs_input):
    """
    !gifs firmino
    """
    if gifs_input==False:
        await bot.say("Missing argument. Example: !gifs firmino")
    else:
        await bot.say(functions.get_gifs(gifs_input))



@bot.command()
async def cat(*number):
    """ 
    !cat or !cat <number> 
    """
    if number:
        inputval = number[0][0]
        if(str(inputval).isdigit()):
            choice = inputval
        else:
            choice = 'x'
    else:
        choice = 'x'
    giflink = functions.cat(choice)
    await bot.say(giflink)



@bot.command()
async def klopp(*number):
    """ 
    !klopp or !klopp <number>
    """
    if number:
        inputval = number[0][0]
        if(str(inputval).isdigit()):
            choice = inputval
        else:
            choice = 'x'
    else:
        choice = 'x'

    giflink = functions.klopp(choice)
    await bot.say(giflink)



@bot.command()
async def wengerout():
    """ 
    Arsenal Fan TV
    """
    arsenal_fan_tv = "https://www.youtube.com/user/arsenalfanstv"
    embed = discord.Embed(title="Arsenal Fan TV", url = arsenal_fan_tv, colour=discord.Colour(0xcc0000))
    await bot.say(embed=embed)



@bot.command()
async def goals(*name):
	"""
    !goals gerrard
    """
	if (name):
		await bot.say(functions.goals(name))
	else:
		await bot.say(functions.goals('gerrard'))



@bot.command()
async def list_help():
    """
    list of inputs for !table, !injuries, !gifs
    """
    embed = discord.Embed(description=functions.list_help(), colour=discord.Colour(0xcc0000))
    await bot.say(embed = embed)



@bot.command()
async def table(*country):
    """
    !table or !table spain
    """
    if country:
        standings = functions.table(country)
    else:
        standings = functions.table()
    embed = discord.Embed(description = standings, colour = discord.Colour(0xcc0000))
    await bot.say(embed=embed)



@bot.command()
async def injuries(*team):
    """
    !injuries or !injuries boro
    """
    if team:
        injury_list = functions.injuries(team)
    else:
        injury_list = functions.injuries(["liverpool"])

    embed = discord.Embed(description = injury_list, color = discord.Colour(0xcc0000))
    await bot.say(embed=embed)


@bot.command()
async def weather(*args):
    """
    !weather London, UK or !weather Portland unit="F"
    """
    args = list(args)
    if len(args) == 0:
        response = "Please enter a location.\nExamples: !weather London, UK\n!weather Portland F"
    else:
        args = [x.lower() for x in args]
        if "f" in args:
            unit = "F"
            args.remove("f")
        else:
            if "c" in args:
                args.remove("c")
            unit = "C" 
        arguments = ' '.join(args)
        location = arguments.strip().replace(" ","")
        response = functions.get_weather(location, unit)
     
    embed = discord.Embed(description = response, color = discord.Colour(0xcc0000))
    embed.set_footer(text="                                                       ")
    await bot.say(embed=embed)

@bot.command()
async def next():
    """
    Next Game Countdown. Ask Liverbird.
    """
    spurs = datetime.datetime(2017, 2, 11, 17, 30)
    now = datetime.datetime.now()
    countdown = relativetd.relativedelta(spurs, now)
    if ( countdown.seconds > 0):
        countdown_display_string = "```{} days {} hours {} minutes {} seconds\n\nLiverpool Vs Spurs at Anfield```".format(countdown.days, countdown.hours, countdown.minutes, countdown.seconds)
        await bot.say(countdown_display_string)
    else:
        await bot.say("No matches entered in the program. Please ask Liverbird.")


bot.loop.create_task(no_context_general())
bot.loop.create_task(subredditfeed())
bot.loop.create_task(twitterfeed())
bot.run(config.token)

