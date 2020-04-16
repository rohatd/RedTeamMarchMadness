from matchup import Matchup
import json

from queue import Queue



class Bracket:

    def __init__(self,matchupQ):
        self.matchupQueue = list(matchupQ)
        self.matchupList = list(matchupQ)
        
    def printQueue(self):
        print(self.matchupQueue)

    #returns json of the teams in the queue
    def get_teams(self):
        return json.dummps(list(self.matchupQueue.queue))

    #evalaute bracket 
    def evaluateBracket(self):
        while len(self.matchupQueue) != 1:
            team1 = self.matchupQueue.pop(0)
            team2 = self.matchupQueue.pop(0)
            teamMatchup = Matchup(team1,team2)
            winner = teamMatchup.randomForestRegressor(2019)
            self.matchupQueue.append(winner)
            self.matchupList.append(winner)
            print("{0} played {1} and the winner is: {2}".format(team1.get_team_name().replace(" NCAA","").replace(" ","-"),team2.get_team_name().replace(" NCAA","").replace(" ","-"),winner.get_team_name().replace(" NCAA","").replace(" ","-")))


    def getBracket(self):
        name_list=[]
        for i in range(len(self.matchupList)):
            name_list.append(self.matchupList[i])
            #name_list.append(self.matchupList[i].get_team_name().replace(" NCAA",""))
        return name_list