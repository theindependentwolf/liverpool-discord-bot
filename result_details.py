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
import csv
import time
import dateutil.relativedelta as relativetd


def next_game():
    """
    Count down to the next game
    """
    current_time = datetime.datetime.now()
    opponent_details = get_opponent_details()
    if opponent_details:
        oppo_time = opponent_details[0]
        opponent_time = datetime.datetime(int(oppo_time[:4]), int(oppo_time[4:6]), int(oppo_time[6:8]), int(oppo_time[9:11]) - 1, int(oppo_time[11:13]))
        countdown = relativetd.relativedelta(opponent_time, current_time)
        countdown_readable = "{} day(s) {} hours {} minutes {} seconds".format(countdown.days, countdown.hours, countdown.minutes, countdown.seconds)
        return "```{}\n{}```".format(countdown_readable, opponent_details[1])
    else:
        return "```No fixtures found in the calendar```"        


def get_opponent_details():
    """
    Return opponent details
    """
    todays_date = time.strftime("%Y%m%d")
    opponent_details = ""
    with open('fixtures.csv','rt') as csvfile:
        content = csv.reader(csvfile, delimiter = ',')
        for row in content:
            date = row[0]
            summary = row[1]
            if date[:8] >= todays_date:
                return row
    

def get_readable_time(input_date):
    """
    Convert yyyymmddT00000000 into readable time
    """
    weekchart = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday",5:"Saturday", 6:"Sunday"}
    readable_time = ""
    separator_slash = "/"
    separator_colon = ":"
    space = " "
    year = input_date[:4]
    month = input_date[4:6]
    date = input_date[6:8]
    hour = input_date[9:11]
    minute = input_date[11:13]
    day = datetime.datetime(int(year), int(month), int(date), 0, 0, 0, 0).weekday()
    return ('{:9s} {}/{}/{} {}:{}'.format(weekchart.get(day), month, date, year, hour, minute))


def get_fixtures():
    """
    Gets the next 5 fixtures according to date
    """
    printable_string ="```"
    todays_date = time.strftime("%Y%m%d")
    count = 1
    with open('fixtures.csv','rt') as csvfile:
        content = csv.reader(csvfile, delimiter=',')
        for row in content:
            date = row[0]
            summary = row[1]
            if date[:8] > todays_date:
                printable_string += get_readable_time(date) + "  " + get_home_away(summary) + "  " + summary.replace("Liverpool","").replace(" v ","").strip() + "\n"
                if count == config.number_of_fixtures:
                    printable_string += "```"
                    return printable_string
                else:
                    count = count + 1

def get_home_away(summary):
    """
    Tells if it's a home or an away fixture
    """
    if summary.startswith('Liverpool'):
        return "home"
    else:
        return "away" 

def ten_games(*team):
    """
    Get the results of the last 10 games for EPL Teams from the BBC Website
    """
    if not team:
        team = "Liverpool"
    else:
        team = team[0]
    url = "http://www.bbc.com/sport/football/premier-league/table"
    html = urllib.request.urlopen(url).read()
    bs = BeautifulSoup(html, "html.parser")
    tables = bs.findChildren('table')

    my_table = tables[0]

    rows = my_table.findChildren(['tr'])

    printable_results = "```"

    for row in rows:
        if row.find('ol'):
            team_name = row.find('td', class_="team-name")
            if team.lower() in team_name.string.lower():
                ten_games = row.find('ol').findChildren(['li'])
                for game in ten_games:
                    printable_results += game.get('title') + "\n"
    printable_results += "```"
    print(printable_results)
#    return printable_results 





def team_form():
    """
    Get the results of the last 10 games for EPL Teams from the BBC Website
    """

    url = "http://www.bbc.com/sport/football/premier-league/table"
    html = urllib.request.urlopen(url).read()
    bs = BeautifulSoup(html, "html.parser")
    tables = bs.findChildren('table')
    my_table = tables[0]
    rows = my_table.findChildren(['tr'])
    position = 1
    printable_form = "```"

    for row in rows:
        if row.find('ol'):
            team_name = row.find('td', class_="team-name")
            print(team_name)
            ten_games = row.find('ol').findChildren(['li'])
            printable_form += str(position).rjust(3) + " " + str(team_name.text.ljust(23)) 
            for game in ten_games:
                printable_form += game.string[0] + " " 
            printable_form += "\n"
            position = position + 1
    printable_form += "```"
#    return printable_form
    print(printable_form)    



