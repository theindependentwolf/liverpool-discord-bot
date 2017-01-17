#AUTHOR: ANIRUTH OBLAH


import discord
from discord.ext import commands
import random
from random import randint
import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import functions




description = ''' Birdie-G, a red avian bot. '''

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



#Tells if the person parsed in the argument is cool

@bot.command(passed_context=True)
async def cool(name):
	"""Determines if someone is cool. Example: !cool Alberto_Moreno"""
	nolist = ['united','everton','manchester','scum','fellaini','mu','utd']
	if(name in nolist):
		await bot.say('No, {} is not cool'.format(name))
	else:
		random_number = randint(1,10)
		if random_number <= 2:
			await bot.say('No, {} is not cool'.format(name))
		else:
			await bot.say('Yes, {} is cool'.format(name))


#Predicts games between two teams

@bot.command()
async def predict(team1: str, team2: str):
	"""Predicts result. Example: !predict Liverpool Spurs"""
	if (team1 and team2):
		result = functions.predict(team1, team2)
		await bot.say(result)
	else:
		await bot.say("Missing arguments. Please mention two teams.")



#Predicts the next Liverpool game

@bot.command()
async def predict_next():
	"""Predicts the next Liverpool FC game"""
	result = functions.predict_next()
	await bot.say(result)




#GIFS - Lucas Unackee gif

@bot.command()
async def lucas():
	"""Unlackee"""
	await bot.say(functions.gifs("lucas"))


#Returns cat gifs

@bot.command()
async def cat(*number):
        """ Cat gifs. Enter optional number for specific gif """
        if (number):
                        inputval = number[0][0]
                        if(str(inputval).isdigit()):
                                choice = inputval
                        else:
                                choice = 'x'
        else:
                choice = 'x'
        giflink = functions.cat(choice)
        await bot.say(giflink)



#Returns a random Klopp gif if number isn't specified. Number of gifs may vary as more are added

@bot.command()
async def klopp(*number):
	""" Klopp gifs. Enter optional number for specific gif """
	if (number):
			inputval = number[0][0]
			if(str(inputval).isdigit()):
				choice = inputval
			else:
				choice = 'x'
	else:
		choice = 'x'
	giflink = functions.klopp(choice)
	await bot.say(giflink)




#Returns a Hendo gif

@bot.command()
async def hendo():
	""" Hendo stare """
	await bot.say(functions.gifs("hendo"))


#returns a lallana gif

@bot.command()
async def lallana():
	""" Lallana """
	await bot.say(functions.gifs("lallana"))



#Table Help - List of countries to be displayed

@bot.command()
async def countries():
	""" To get a list of countries available for table command """
	printable_string = functions.countries()
	await bot.say(printable_string)



#Standings of different leagues


@bot.command()
async def table(*country):
	"""Shows the Premier League Table. !table country_name for others"""
	if(country):
		standings = functions.table(country) 
	else:
		standings = functions.table()
	await bot.say(standings)
	#print(printablestring)


# Get a list of commands for different team names

@bot.command()
async def injuries_teams():
	"""List of team names for injuries list """
	await bot.say(functions.injuries_teams())


#command to get injury list for different teams. Default is Liverpool FC

@bot.command()
async def injuries(*team):
	"""Shows a list of injuries. Example: !injuries team_name"""
	if(team):
		await bot.say(functions.injuries(team))
	else:
		await bot.say(functions.injuries('liverpool'))



#Get bot token from the discord developer page

bot.run(bot_token)


