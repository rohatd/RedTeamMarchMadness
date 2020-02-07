import requests
from urllib2 import urlopen
import time
import json
from bs4 import BeautifulSoup

"""
        Scraper for acquiring data from NCAA's official website
            All scraped data is dumped to scrapeData.json
"""
IDs = {}
players = {}
teamIDs = []
teamNames = {}

# Generates dict of [teamID, teamName] pairs
# Team ID's are scraped from NCAA for accessing team stats webpage
def getIDs():
    idURL = 'http://stats.ncaa.org/game_upload/team_codes'
    response = requests.get(idURL)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.findAll('tr')
    for tr in rows:
        teamID = tr.findNext('td').contents[0]
        teamIDs.append(teamID)
        team = tr.find(text=teamID).findNext('td').contents[0]
        teamNames[teamID] = team

# Substantiates IDs (nested dict) with all team stats from NCAA's website
# teamArgs = array of strings containing team names to scrape
def getStats(teamArgs):
    reversedNames = dict(map(reversed, teamNames.items()))
    for teamName in teamArgs:
        if reversedNames.get(teamName) == None:
            print "Cannot find school with name " + teamName
            return
        statsUrl = "http://stats.ncaa.org/team/" + reversedNames[teamName] + "/14300";
        response = requests.get(statsUrl)
        soup = BeautifulSoup(response.text, "html.parser")

        tab = soup.find("table",{"class":"mytable"})
        tempDict = {}
        if tab != None:
            rows = tab.findAll('tr')
            for row in rows:
                teamStats = row.findAll('td')
                if row.find('a') != None and len(teamStats) == 3:
                    stat = row.find('a').contents[0]
                    val = teamStats[2].contents[0].strip()
                    tempDict[stat] = val
        IDs[teamName] = tempDict
    with open('scrapeData.json', 'w') as fp:
        json.dump(IDs, fp, indent = 4)

# Substantiates players dict with [teamName, playerStats] pairs
# teamName = string, playerStats = array with all stat values
# teamArgs = array of strings containing team names to scrape
def getPlayerStats(teamArgs):
    reversedNames = dict(map(reversed, teamNames.items()))
    for teamName in teamArgs:
        players[teamName] = {}
        if reversedNames.get(teamName) == None:
            print "Cannot find school with name " + teamName
            return
        statsUrl = "http://stats.ncaa.org/team/" + reversedNames[teamName] + "/stats/15061"
        response = requests.get(statsUrl)
        soup = BeautifulSoup(response.text, "html.parser")
        tab = soup.find("table",{"id":"stat_grid"})
        for row in tab.findAll('tr'):
            playerName = ""
            playerStats = []
            for td in row.findAll('td'):
                playerStats.append(td.get_text().strip())
            if len(row.findAll('td')) > 0:
                playerName = row.findAll('td')[1].get_text()
                players[teamName][playerName] = playerStats
    with open('scrapeData.json', 'w') as fp:
        json.dump(players, fp, indent = 4)

getIDs()
time.sleep(1)
