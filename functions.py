import discord
from random import randint
import random
import random
from random import randint
import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup



#Predicts the result between two teams. Works on Random Numbers. Favors Liverpool slightly

def predict(team1: str, team2: str):
	liverpool = ['lfc', 'liverpool', 'liverpoolfc']
	utd = ['scum','utd','mancs','manchester','united']

	chance = randint(0,10)
	if(chance > 7):
		team1_score = randint(0,5)
		team2_score = randint(0,5)
	else:
		team1_score = randint(0,3)
		team2_score = randint(0,3)


	if(team1 in liverpool):
		team1_score += 1
	elif(team1 in utd):
		if (team1_score > 0):
			team1_score -= 1
	

	
	if(team2 in liverpool):
		team2_score += 1
	elif(team2 in utd):
		if (team2_score > 0):
			team2_score -= 1

	
	
	
	return ( team1 + str(team1_score).rjust(2) + " - " + str(team2_score).ljust(2) + team2 )



#Predicts Liverpool's next result


def predict_next():
	lfc = randint(0,7)
	if (lfc < 5):
		result = "Liverpool will win the next game."
	elif(lfc > 4 and lfc < 7):
		result = "Liverpool will draw the next game."
	else:
		result = "Liverpool will lose the next game :( "
	return (result)



#Contains gif links


def gifs(case: str):
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
		'woydance':'http://media0.giphy.com/media/3oEjHE8cahZQc9ZXa0/giphy.gif'
		
	}
	return switcher.get(case, "not found")	


#Contains links to goals


def goals(name):
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

	return goaldict.get(name[0],notfound)
	


# Returns cat gifs


def cat(number):
	cat_list = ["https://gfycat.com/CornyGleamingJoey", "https://gfycat.com/LateUnknownGossamerwingedbutterfly", "https://gfycat.com/CloseMediocreEland", "https://gfycat.com/VigorousCraftyGopher", "http://imgur.com/gIdpXMF", "http://imgur.com/FJzfQDN", "http://imgur.com/IrbGz3l"]
	
	choice = number
	if(choice!='x'):
		return(cat_list[(int(choice) % len(cat_list))])
	else:
		return(random.choice(cat_list))


# Returns Klopp gifs
		

def klopp(number):
	klopp_list = ["https://gfycat.com/WelltodoPoorAfricangoldencat","https://gfycat.com/LegalZealousBurro","https://gfycat.com/DangerousForcefulLamb","http://imgur.com/KJxX3ba","https://gfycat.com/HeavyBitesizedBlueandgoldmackaw", "http://imgur.com/fesRVRn","https://media.giphy.com/media/xTiTngTp9RkZAbePOo/giphy.gif","https://gfycat.com/ArtisticThatGreatdane", "https://gfycat.com/WeirdAlienatedKitten","http://tmp.fnordig.de/klopp-facepalm.gif"]
		
	choice = number

	if(choice!='x'):
		return(klopp_list[(int(choice) % len(klopp_list))])
	else:
		return(random.choice(klopp_list))



# Contains a list of countries for table commands

def countries():
	countries_list = "```To get the standings for different leagues, !table country_name\nExample: !table scotland\n\nList of countries: \n\nengland\nfrance\ngermany\nitaly\nchamp (for championship)\nnl (for Dutch League)\nrussia\naus (for Australian League)\nturkey\nscotland\nireland\nusa for USA EAST\nusawest for USA WEST```"
	return countries_list



# Returns table for specific country. Default is Liverpool. Parsed from BBC Wesbite.

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
		'ireland':'http://www.bbc.com/sport/football/league-of-ireland-premier/table'
		}
	if(country):
		league = str(country[0][0]).strip().lower()
		if (league in url_dict):
			url = url_dict[league]
		else:
			league = 'england'
			url = url_dict[league]
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
	table_list.append("------------------------------------------------------------")
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



# List of teams for for which injuries are avilable


def injuries_teams():
	team_list = ["hull","sunderland","saints","palace","watford","stoke","arsenal","everton","liverpool","whu - For West Ham","swansea","wba - For West Brom","city - For Man City","burnley","spurs","boro - For Middlesborough","united - For Scum","leicester","chelsea","bournemouth"]
	printable_string = "\n".join(team_list)
	printable_string = "```" + printable_string + "```"
	return(printable_string)
	



# Returns injuries. Default is Liverpool.

def injuries(team):
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
	
	team_name = teams.get(team[0].strip().lower(), 'Liverpool away shirt')

	url = "http://www.physioroom.com/news/english_premier_league/epl_injury_table.php"
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, "html.parser")
	lp = soup.find(alt=team_name).parent.parent.parent.next_sibling.next_sibling
	if(not lp):
		return("```No reported injuries.```")
	player_info = ""
	heading = "Name".ljust(15) + "Injury".ljust(25) + "Return Date".ljust(15) + "\n" + "-----------------------------------------------------------" + "\n"
	player_list = []
	player_list.append(heading)

	while True:
		if(lp.has_attr('id')):
	        	break
		else:
			tdlist = lp.find_all('td')#	player_info = tdlist[0].string+"\t"+tdlist[1].string+"\t"+tdlist[3].string
			if(tdlist[1].find('a')):
				player_info = str(tdlist[0].string.strip()).ljust(15) + str(tdlist[1].find('a').string.strip()).ljust(25)  + str(tdlist[3].string.strip()).ljust(15)
				player_list.append(player_info.strip())
			else:
				player_info = str(tdlist[0].string.strip()).ljust(15) + str(tdlist[1].string.strip()).ljust(25) + str(tdlist[3].string.strip()).ljust(15)
				player_list.append(player_info.strip())
		lp=lp.findNext('tr')
	printable_string = "\n".join(player_list)
	printable_string = "```" + printable_string + "```"
	return(printable_string)



# Reads every message in the chat and processes them

def processMessage(message, bot):
	swear_words = ['cunt','fuck','fucking','poo', 'shit', 'poop', 'piss', 'ass', 'faggot','nigger','asshole','kunt']
	
	channel = bot.get_channel('269658482238554113')

	if message.author == bot.user:
		return 
		
	# Says hi to Liverbird

	if message.author.id == '195628542233411593' and "hey" in message.content:
		return "Hi " + message.author.nick

	# Directs user to politics channel when trump is mentioned
	
	if "trump" in message.content.lower() and message.channel != channel:
		return "Please head over to {0.mention}. MAGA.".format(channel)


	# Discplines user when strong language is used. Frequency is hard-coded.

	if any(word in message.content.lower() for word in swear_words):
		if randint(0,25) == 7:
			return "Please watch your language sir, {0.author.mention}".format(message)
		else:
			return
