import discord
from discord.ext import commands
import random
from random import randint
import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import functions



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
    # we do not want the bot to reply to itself
	response = functions.processMessage(message, bot)
	if response:
		await bot.send_message(message.channel, response)
	await bot.process_commands(message)


@bot.command(pass_context=True)
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

@bot.command()
async def predict(team1: str, team2: str):
	"""Predicts result. Example: !predict Liverpool Spurs"""
	if (team1 and team2):
		result = functions.predict(team1, team2)
		await bot.say(result)
	else:
		await bot.say("Missing arguments. Please mention two teams.")


@bot.command()
async def predict_next():
	"""Predicts the next Liverpool FC game"""
	result = functions.predict_next()
	await bot.say(result)




#GIFS

@bot.command()
async def lucas():
	"""Unlackee"""
	await bot.say(functions.gifs("lucas"))




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


@bot.command()
async def hendo():
	""" Hendo stare """
	await bot.say(functions.gifs("hendo"))


@bot.command()
async def lallana():
	""" Lallana """
	await bot.say(functions.gifs("lallana"))


@bot.command()
async def nam():
	""" Flashback """
	await bot.say(functions.gifs("nam"))


@bot.command()
async def disappoint():
	""" Stevie and Carra disappointed """
	await bot.say(functions.gifs("disappoint"))


@bot.command()
async def gerrard():
	""" Steven Gerrard """
	await bot.say(functions.gifs("gerrard"))


@bot.command()
async def bobby():
	""" Bobby skills """
	await bot.say(functions.gifs("bobby"))



@bot.command()
async def dance():
	""" Sturridge animation dance """
	await bot.say(functions.gifs("dance"))


@bot.command()
async def ffs():
	""" FFS Brendan """
	await bot.say(functions.gifs("ffs"))



@bot.command()
async def everton():
	""" Everton """
	await bot.say(functions.gifs("everton"))


@bot.command()
async def woydance():
	""" Woy Dance """
	await bot.say(functions.gifs("woydance"))


@bot.command()
async def suarez():
	""" Suarez """
	await bot.say(functions.gifs("suarez"))


@bot.command()
async def wengerout():
	""" Link to Arsenal Fan TV """
	await bot.say('https://www.youtube.com/user/arsenalfanstv')



@bot.command()
async def goals(*name):
	"""Goal Gifs. Example !goals gerrard """
	if (name):
		await bot.say(functions.goals(name))
	else:
		await bot.say(functions.goals('gerrard'))




#Table Help - List of countries to be displayed

@bot.command()
async def countries():
	""" To get a list of countries available for table command """
	printable_string = functions.countries()
	await bot.say(printable_string)



#Table


@bot.command()
async def table(*country):
	"""Shows the Premier League Table. !table country_name for others"""
	if(country):
		standings = functions.table(country) 
	else:
		standings = functions.table()
	await bot.say(standings)
	#print(printablestring)


@bot.command()
async def injuries_teams():
	"""List of team names for injuries list """
	await bot.say(functions.injuries_teams())


@bot.command()
async def injuries(*team):
	"""Shows a list of injuries. Example: !injuries team_name"""
	if(team):
		await bot.say(functions.injuries(team))
	else:
		await bot.say(functions.injuries('liverpool'))



bot.run('token')
