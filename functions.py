import discord
from random import randint
import random
import random
from random import randint
import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import nocontext
import requests
import datetime
import config
import asyncio


def predict(team1: str, team2: str):
    """
    Predicts results between two teams. 
    """
    liverpool = ['lfc', 'liverpool', 'liverpoolfc']

    chance = randint(0,10)
    if chance > 7:
        team1_score = randint(0,5)
        team2_score = randint(0,5)
    else:
        team1_score = randint(0,3)
        team2_score = randint(0,3)

    if team1.lower().strip() in liverpool:
        team1_score += 1    
    if team2.lower().strip() in liverpool:
        team2_score += 1
	
    return (team1 + str(team1_score).rjust(2) + " - " + str(team2_score).ljust(2) + team2)



def get_gifs(case: str):
    """
    Returns a gif based on the input
    """
    
    switcher = {
		'lucas': "https://m.popkey.co/1e495f/LlpVq.gif",
		'lallana': "https://gfycat.com/ThirstyTotalFlounder",
		'hendo': "https://giant.gfycat.com/PopularAcceptableHawaiianmonkseal.gif",
		'wij':"http://cdn.images.express.co.uk/img/dynamic/galleries/x701/152689.jpg",
		'disappoint':'https://31.media.tumblr.com/25277ed25bab911a828c24ea938f74c7/tumblr_inline_myxmcqEy3k1qc9aza.gif',
		'nam':'https://i.imgur.com/VgVjotr.gif',
		'ffs':'https://gfycat.com/JubilantNimbleJackrabbit',
		'gerrard':'http://i.imgur.com/5oGaBFu.gif',
		'bobby':'http://imgur.com/VshfmIO',
		'dance':'http://giphy.com/gifs/lfc-i1MGZo7GHZFte',
		'everton':'https://cdn.meme.am/instances/49057267.jpg',
		'suarez':'https://greatrednorth.files.wordpress.com/2013/04/luis-ivanovic.gif?w=510',
		'woydance':'http://media0.giphy.com/media/3oEjHE8cahZQc9ZXa0/giphy.gif',
        'help':'Example: !gifs lallana\nGifs present: lucas, lallana, hendo, wij, disappoint, nam, ffs, gerrard, bobby, dance, everton, suarez, woydance. More to be added.'
	}
    
    return (switcher.get(case, "not found. Use !gifs help."))	




def goals(name):
    """
    Returns a goal based on the input
    """
    notfound = "http://giphy.com/gifs/internet-google-chrone-9J7tdYltWyXIY"
    goaldict = {
		'gerrard':'https://www.youtube.com/watch?v=4sBxm8Qo4sY',
		'riise':'https://youtu.be/tx8tMiaNawI?t=30s',
		'kolo':'https://www.youtube.com/watch?v=B7quD8H_75E',
		'lovren':'https://www.youtube.com/watch?v=LJV5xkj_3SA',
		'suarez':'https://www.youtube.com/watch?v=iX8eZn9uFU4',
		'xabi':'https://www.youtube.com/watch?v=DuZd0n8MqWs',
		'lallana':'https://www.youtube.com/watch?v=7oBfGmrmQ8c',
		'istanbul':'https://www.youtube.com/watch?v=tnB4XAhl6PY'
	}

    return (goaldict.get(name[0],notfound))	



def cat(number):
    """
    Returns a random cat if number not specified
    """
    cat_list = ["https://gfycat.com/CornyGleamingJoey", "https://gfycat.com/LateUnknownGossamerwingedbutterfly", "https://gfycat.com/CloseMediocreEland", "https://gfycat.com/VigorousCraftyGopher", "http://imgur.com/gIdpXMF", "http://imgur.com/FJzfQDN", "http://imgur.com/IrbGz3l"]
    
    choice = number
    if choice != 'x':
        return cat_list[(int(choice) % len(cat_list))]
    else:
        return (random.choice(cat_list))



def klopp(number):
    """
    Returns a random Klopp gif unless number specified
    """
    klopp_list = ["https://gfycat.com/WelltodoPoorAfricangoldencat","https://gfycat.com/LegalZealousBurro","https://gfycat.com/DangerousForcefulLamb","http://imgur.com/KJxX3ba","https://gfycat.com/HeavyBitesizedBlueandgoldmackaw", "http://imgur.com/fesRVRn","https://media.giphy.com/media/xTiTngTp9RkZAbePOo/giphy.gif","https://gfycat.com/ArtisticThatGreatdane", "https://gfycat.com/WeirdAlienatedKitten","http://tmp.fnordig.de/klopp-facepalm.gif"]
    
    choice = number
    if(choice!='x'):
        return (klopp_list[(int(choice) % len(klopp_list))])
    else:
        return (random.choice(klopp_list))



def list_help():
    """
    Returns a list of available inputs tables, injuries, goals
    """
    goals = "gerrard, riise, kolo, suarez, xabi, lallana, istanbul"
    table = "england, champ, league1, league2, scotland, aus, germany, italy, france, turkey, usa, usawest, spain, russia, nl(for holland), ireland, russia"
    injuries = "hull, sunderland, saints, palace, watford, stoke, arsenal, everton, liverpool, whu, swansea, wba, city, burnley, spurs, united, leicester, boro, chelsea, bournemouth"
    gifs = "lallana, wij, hendo, firmino, nam, disappoint, ffs, woydance, dance, gerrard, suarez, everton"    
    
    list_help_string = "**goals:** {}\n\n**table:** {}\n\n**injuries:** {}\n\n**gifs:** {}".format(goals, table, injuries, gifs)
    return list_help_string



def table(*country):
    url_dict = {'england':'http://www.bbc.com/sport/football/premier-league/table',
        'spain':'http://www.bbc.com/sport/football/spanish-la-liga/table',
        'italy':'http://www.bbc.com/sport/football/italian-serie-a/table',
        'germany':'http://www.bbc.com/sport/football/german-bundesliga/table',
        'scotland':'http://www.bbc.com/sport/football/scottish-premiership/table',
        'turkey':'http://www.bbc.com/sport/football/turkish-super-lig/table',
        'france':'http://www.bbc.com/sport/football/french-ligue-one/table',
        'usa':'http://www.bbc.com/sport/football/us-major-league/table',
        'usawest':'http://www.bbc.com/sport/football/us-major-league/table',
        'russia':'http://www.bbc.com/sport/football/russian-premier-league/table',
        'champ':'http://www.bbc.com/sport/football/championship/table',
        'nl':'http://www.bbc.com/sport/football/dutch-eredivisie/table',
        'aus':'http://www.bbc.com/sport/football/australian-a-league/table',
        'ireland':'http://www.bbc.com/sport/football/league-of-ireland-premier/table',
        'league1':'http://www.bbc.com/sport/football/league-one/table',
        'league2':'http://www.bbc.com/sport/football/league-two/table'
        }
    if(country):
        league = str(country[0][0]).strip().lower()
        if (league in url_dict):
            url = url_dict[league]
        else:
            return "Not Found. Use !list_help."
    else:
        league = 'england'
        url = url_dict[league]

    html = urllib.request.urlopen(url).read()
    bs = BeautifulSoup(html, "html.parser")
    tables = bs.findChildren('table')
    if(league == 'usawest'):
        prem_table = tables[1]
    else:
        prem_table = tables[0]
    rows = prem_table.findChildren('tr')
    skip = 0
    skip_row = 0
    count = 1
    table_list = []
    printablestring = ""
    heading = "No.".ljust(3) + "Team Name".ljust(21)
    for i in ['P','W','D','L','GF','GA','GD','PTS']:
        heading += str(i).rjust(4)
    table_list.append(heading)
    table_list.append("--------------------------------------------------------")
    for row in rows:
        if(skip_row <= 1):
            skip_row += 1
            continue
        team_info = str(count).ljust(3)
        cells = row.findChildren('td')
        for cell in cells:
            if skip == 0 or skip == 1 or skip == 11 or skip == 12 :
                skip = skip + 1
                continue
            value = cell.string
            if skip == 2:
                team_name = value[0:20]
                team_info += str(team_name).ljust(21)
            else:
                team_info += value.rjust(4)
            skip = skip + 1
        table_list.append(team_info)
        skip = 0
        count += 1


    printablestring = '\n'.join(table_list)
    printablestring = "```" + printablestring + "```"
    return(printablestring)


def injuries(team):
    """
    Returns injuries for the specified teams
    """
    teams={'hull':'Hull City away shirt',
		'sunderland':'Sunderland away shirt',
		'saints':'Southampton away shirt',
		'palace':'Crystal Palace away shirt',
		'watford':'Watford away shirt',
		'stoke':'Stoke City away shirt',
		'arsenal':'Arsenal away shirt',
		'everton':'Everton away shirt',
		'liverpool':'Liverpool away shirt',
		'whu':'West Ham United away shirt',
		'swansea':'Swansea City away shirt',
		'wba':'West Bromwich Albion away shirt',
		'city':'Manchester City away shirt',
		'burnley':'Burnley away shirt',
		'spurs':'Tottenham Hotspur away shirt',
		'boro':'Middlesbrough away shirt',
		'united':'Manchester United away shirt',
		'leicester':'Leicester City away shirt',
		'chelsea':'Chelsea away shirt',
		'bournemouth':'Bournemouth away shirt'}
   
    team_name = teams.get(team[0].strip().lower(), 'Not Found')
    if team_name == "Not Found":
        return "Not Found. Use !list_help."
    url = "http://www.physioroom.com/news/english_premier_league/epl_injury_table.php"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    lp = soup.find(alt=team_name).parent.parent.parent.next_sibling.next_sibling
    if(not lp):
        return("```No reported injuries.```")
    player_info = ""
    heading = "Name".ljust(15) + "Injury".ljust(20) + "Return Date".ljust(15) + "\n" + "--------------------------------------------------------" + "\n"
    player_list = []
    player_list.append(heading)
    
    while True:
        if(lp.has_attr('id')):
            break
        else:
            tdlist = lp.find_all('td')#	player_info = tdlist[0].string+"\t"+tdlist[1].string+"\t"+tdlist[3].string
            if(tdlist[1].find('a')):
                player_info = str(tdlist[0].string.strip()).ljust(15) + str(tdlist[1].find('a').string.strip()).ljust(20)  + str(tdlist[3].string.strip()).ljust(15)
                player_list.append(player_info.strip())
            else:
                player_info = str(tdlist[0].string.strip()).ljust(15) + str(tdlist[1].string.strip()).ljust(20) + str(tdlist[3].string.strip()).ljust(15)
                player_list.append(player_info.strip())
        lp=lp.findNext('tr')
    printable_string = "\n".join(player_list)
    printable_string = "```" +printable_string + "```"
    return(printable_string)



def get_weather(location, unit):
    """
    Get weather information about a location
    """
    location = location.replace(" ","")
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location, config.openweather_api_key)
    weather = requests.get(url).json()
    if weather['cod'] == "502":
        response = "Error: Not found city"
        return response
    else:
        if unit == "C":
            temp_unit = "C"
            temp = int(weather['main']['temp'] - 273.15)
            temp_max = int(weather['main']['temp_max'] - 273.15)
            temp_min = int(weather['main']['temp_min'] - 273.15)
        elif unit == "F":
            temp_unit = "F"
            temp = int(weather['main']['temp'] * (9/5) - 459.67)
            temp_max = int(weather['main']['temp_max'] * (9/5) - 459.67)
            temp_min = int(weather['main']['temp_min'] * (9/5) - 459.67)
        
        description = weather['weather'][0]['description']
        humidity = weather['main']['humidity']
        wind_kmph = weather['wind']['speed'] * 3.6
        location_name = weather['name']
        location_country = weather['sys']['country']
        response = "Location: **{}, {}**\nDescription: **{}**\nTemp: **{} {}**\nMax/Min Temp: **{}/{} {}**\nHumidity: **{} %**\nWind Speed: **{:0.1f} kmph**".format(location_name, location_country, description, temp, temp_unit, temp_max, temp_min, temp_unit, humidity, wind_kmph)       
        
        return response


async def processMessage(message, bot):
    """
    Processes Incoming Messages and sends responses accordingly
    """
    swear_words = ['cunt','fuck','fucking','poo', 'shit', 'poop', 'piss', 'ass', 'faggot','nigger','asshole','kunt', 'bitch']
    bot_shitty = ['shit','shitty','cunt']    
    bot_shitty_response = ['Fuck off, you shitty human!', 'shit human!', 'fuck off!', 'cunt!', 'twat!', 'you little shit!', 'fgt'] 
    

    channel = bot.get_channel('269658482238554113')
    
    if message.author == bot.user:
        return

    #Reply to 'shitty bot' messages
    if "bot" in message.content.lower().split() and any(word in message.content.lower().split() for word in bot_shitty):
        await asyncio.sleep(1)
        return random.choice(bot_shitty_response)


    #Ask birdie for shower thoughts
    if str(message.content).lower().strip() == "birdie shower":
        nocontext_message = nocontext.shower_birdie()
        return(nocontext_message)

    #Ask birdie for advice
    if str(message.content).lower().strip() == "need advice" or str(message.content).lower().strip() == "really need advice":
        advice_category = str(message.content).lower().strip()
        nocontext_message = nocontext.give_advice(advice_category)
        return(nocontext_message)

    #Don't curse at birdie
    if "fuck you birdie" in message.content.lower():
        await asyncio.sleep(2)
        return "Fuck you, {0.author.mention}".format(message)

    if "fuck off birdie" in message.content.lower():
        await asyncio.sleep(2)
        return "No! You fuck off cunt! {}".format(message.author.mention)

    if "stupid bot" in message.content.lower():
        await asyncio.sleep(2)
        return "Stupid human!"
		
	# Says hi to Liverbird

    if message.author.id == '195628542233411593' and "hey" in message.content:
        return "Hi " + message.author.nick


    # Directs user to politics channel when trump is mentioned
	
    if "trump" in message.content.lower().split() and message.channel != channel:
        return "Please head over to {0.mention}. MAGA.".format(channel)


    # Discplines user when strong language is used. Frequency is hard-coded.

    if any(word in message.content.lower().split() for word in swear_words):
        if randint(0,400) == 7:
            return "Please watch your language sir, {0.author.mention}".format(message)
        else:
            return

    if "male models" in message.content.lower():
        await asyncio.sleep(2)
        return "No one cares " + message.author.nick
