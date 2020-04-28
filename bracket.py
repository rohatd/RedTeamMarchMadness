"""Bracket Module

This module represents an entire tournament bracket for March Madness
A bracket consists of a matchup queue consisting of 32 Matchup modules.
A Matchup module consists of two Team modules, so a Bracket should have 64 Teams

"""
import json
from matchup import Matchup


class Bracket:
    """Bracket Class

    Args:
    matchupQ (list):    list of 64 team modules

    Attributes:
        matchupQ (list):    list of 64 team modules
        matchup_list (list):    list of 127 teams, beginning with the first 64
                                and appending the winners for each round
    """

    def __init__(self, matchupQ):
        """initializes Bracket module"""
        self.matchup_queue = list(matchupQ)
        self.matchup_list = list(matchupQ)

    def print_queue(self):
        """prints matchup queue"""

        print(self.matchup_queue)

    def get_teams(self):
        """get list of initial 64 teams

        returns:    list of teams in matchup_queue
        """
        return json.dumps(list(self.matchup_queue))

    def evaluate_bracket(self):
        """evaluates bracket

            Uses a random forest regressor to find the result of each matchup.
            Appends winner of each matchup to the original matchup queue until
            no more teams can be added and queue is empty

            Lists bracket order into matchup list

        """
        while len(self.matchup_queue) != 1:
            team1 = self.matchup_queue.pop(0)
            team2 = self.matchup_queue.pop(0)
            team_matchup = Matchup(team1, team2)
            winner = team_matchup.random_forest_regressor(2019)
            self.matchup_queue.append(winner)
            self.matchup_list.append(winner)
            print("{0} played {1} and the winner is: {2}".format(team1.get_team_name()\
                .replace(" NCAA", "").replace(" ", "-"), team2.get_team_name().replace(" NCAA", "")\
                .replace(" ", "-"), winner.get_team_name().replace(" NCAA", "").replace(" ", "-")))


    def get_bracket(self):
        """returns list of teams in bracket order

        return:
            name_list (list):   list of team names in bracket
        """
        name_list = []
        for i in range(len(self.matchup_list)):
            name_list.append(self.matchup_list[i].get_team_name().replace(" NCAA", ""))
        return name_list
