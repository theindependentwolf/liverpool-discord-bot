import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import config



def get_scores(*league):
    """
    Scrape livescores.com to get live scores
    """
    url_dict = {
            "epl":"http://www.livescores.com/soccer/england/premier-league/"
    }

    if league:
        url = url_dict.get(league[0].strip().lower(), 'Not Found')
        if url == "Not Found":
            return "!list_help for options help"
    else:
        url = url_dict.get("epl")
    
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    #Get the Content Class
    useful = soup.find(class_="content")

    #Remove all useless content. Make useful actually useful.
    del useful.contents[-11:]
    del useful.contents[0::2]
    del useful.contents[0]

    useful_list = useful.contents
    scores_list = get_scores_list(useful_list)
    scores_string = "\n".join(scores_list)
    scores_string = "```" + scores_string.strip() + "```"

    return scores_string

    
def get_scores_list(useful_list):

    #Scores List
    scores_list = []
    
    #Go down the useful content and get all match information and dates

    for useful_contents in useful_list:
        if useful_contents.find(class_="right"):
            match_date = useful_contents.find(class_="right").string.strip()
            scores_list.append("\n" + match_date + "\n")
        else:
            #Match Time
            if len(useful_contents.find(class_="min").contents) == 2:
                match_time = useful_contents.find(class_="min").contents[1].strip()
            elif useful_contents.find(class_="min").string:
                match_time = useful_contents.find(class_="min").string.strip()
            else:
                match_time = "post"

            #Score
            if useful_contents.find(class_="sco").find("a"):
                match_score = useful_contents.find(class_="sco").find("a").string.strip()
            else:
                match_score = useful_contents.find(class_="sco").string.strip()

            home_team = useful_contents.find(class_="ply tright name").string.strip()
            away_team = useful_contents.find(class_="ply name").string.strip()
            
            scoreline = "{:<8}{:>20} {} {:<20}".format(match_time, home_team, match_score, away_team)
            scores_list.append(scoreline)

    return scores_list    
