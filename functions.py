from random import randint
import random
import random
from random import randint
import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup



def predict(team1: str, team2: str):
	team1_score = randint(0,3)
	team2_score = randint(0,3)
	
	return ( team1 + str(team1_score).rjust(2) + " - " + str(team2_score).ljust(2) + team2 )


def predict_next():
	lfc = randint(0,7)
	if (lfc < 5):
		result = "Liverpool will win the next game."
	elif(lfc > 4 and lfc < 7):
		result = "Liverpool will draw the next game."
	else:
		result = "Liverpool will lose the next game :( "
	return (result)


def gifs(case: str):
	switcher = {
		'lucas': "https://m.popkey.co/1e495f/LlpVq.gif",
		'lallana': "https://gfycat.com/ThirstyTotalFlounder",
		'hendo': "https://giant.gfycat.com/PopularAcceptableHawaiianmonkseal.gif",
		'wij':"http://cdn.images.express.co.uk/img/dynamic/galleries/x701/152689.jpg",
	}	
	return switcher.get(case, "not found")





def cat(number):
	cat_list = ["https://gfycat.com/CornyGleamingJoey", "https://gfycat.com/LateUnknownGossamerwingedbutterfly", "https://gfycat.com/CloseMediocreEland", "https://gfycat.com/VigorousCraftyGopher", "http://imgur.com/gIdpXMF", "http://imgur.com/FJzfQDN", "http://imgur.com/IrbGz3l"]
	
	choice = number
	if(choice!='x'):
		return(cat_list[(int(choice) % len(cat_list))])
	else:
		return(random.choice(cat_list))



		

def klopp(number):
	klopp_list = ["https://gfycat.com/WelltodoPoorAfricangoldencat","https://gfycat.com/LegalZealousBurro","https://gfycat.com/DangerousForcefulLamb","http://imgur.com/KJxX3ba","https://gfycat.com/HeavyBitesizedBlueandgoldmackaw", "http://imgur.com/fesRVRn","https://media.giphy.com/media/xTiTngTp9RkZAbePOo/giphy.gif","https://gfycat.com/ArtisticThatGreatdane", "https://gfycat.com/WeirdAlienatedKitten","http://tmp.fnordig.de/klopp-facepalm.gif"]
		
	choice = number

	if(choice!='x'):
		return(klopp_list[(int(choice) % len(klopp_list))])
	else:
		return(random.choice(klopp_list))



def countries():
	countries_list = "```To get the standings for different leagues, !table country_name\nExample: !table scotland\n\nList of countries: \n\nengland\nfrance\ngermany\nitaly\nchamp (for championship)\nnl (for Dutch League)\nrussia\naus (for Australian League)\nturkey\nscotland\nireland\nusa for USA EAST\nusawest for USA WEST```"
	return countries_list




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



def injuries_teams():
	team_list = ["hull","sunderland","saints","palace","watford","stoke","arsenal","everton","liverpool","whu - For West Ham","swansea","wba - For West Brom","city - For Man City","burnley","spurs","boro - For Middlesborough","united - For Scum","leicester","chelsea","bournemouth"]
	printable_string = "\n".join(team_list)
	printable_string = "```" + printable_string + "```"
	return(printable_string)
	



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
