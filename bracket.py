from Queue import Queue
from matchup import Matchup
import json



class Bracket:

    def __init__(self,matchupQueue):
        if(len(matchupQueue) == 4):
            self.matchupQueue =matchupQueue
        else:
            raise ValueError("Queue did not contain 64 teams")

    def printQueue(self):
        print(self.matchupQueue)

    def get_teams(self):
        return json.dummps(list(self.matchupQueue.queue))

    def evaluateBracket(self):
        while len(self.matchupQueue) != 1:
            team1 = self.matchupQueue.popleft()
            team2 = self.matchupQueue.popleft()
            teamMatchup = Matchup(team1,team2)
            winner = teamMatchup.getWinner()
            self.matchupQueue.append(winner)
            print("{0} played {1} and the winner is: {2}".format(team1,team2,winner))
