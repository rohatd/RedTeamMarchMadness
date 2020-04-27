from team import Team
from matchup import Matchup
from bracket import *
import pandas as pd

from queue import Queue

class SeasonData:


    def __init__(self, year, coach_file, basic_file, adv_file):
        self.teams = {}
        self.year = year
        self.matchups = []
        self.bracket = None  # Initial bracket is blank

        coach_df = None
        bas_df = None
        adv_df = None
        # Load data files
        try:
            coach_df = pd.read_csv(coach_file, header=[1])
            coach_df = coach_df.drop(["W", "L", "W-L%", "AP Pre", "AP Post", "NCAA Tournament"], axis=1)
        except:
            print("Error loading coach data csv.")
        try:
            bas_df = pd.read_csv(basic_file, header=[1])
        except:
            print("Error loading basic data csv.")
        try:
            adv_df = pd.read_csv(adv_file, header=[1])
        except:
            print("Error loading advanced data csv.")

        if (coach_df is not None) and (bas_df is not None):
            # If dataframes are passed, initialize teams.
            # TODO: accommodate adv_df

            # Iterate through adv and basic data frames to fill
            # out team informations into Team objects, stored in
            # self.teams
            merged_inner = pd.merge(left=bas_df, right=adv_df, left_on='School', right_on='School')
            #numTeams = merged_inner.shape[0]
            #print(numTeams)
            num_teams = bas_df.shape[0]
            for i in range(num_teams):
                team_row = merged_inner.loc[i,:]
                #print("Dhruv's way", team_row)
                #print("Mario's way", bas_df.loc[i, :])
                #team_row = bas_df.loc[i,:]
                team_name = team_row['School']
                # Trim 'NCAA' from the name
                if "NCAA" in team_name:
                    team_name = team_name[:-5]
                # Get coach data (single row corresponding to school name.)
                coach_row = coach_df.loc[coach_df['School'] == team_name].squeeze()
                self.teams[team_name] = Team(self.year, team_row, coach_row)
            # TODO: accommodate advanced info dataframe by combining it with
            # team_row created from basic dataframe.


    # Getters
    def get_team(self, team_name):
        # Returns Team object
        return self.teams[team_name]

    def get_matchups(self):
        # Returns stored list of matchups, to be used however.
        # Likely as init arg to form Bracket object.
        return self.matchups

    # Mutators (Add / Remove)
    def new_matchup(self, team1, team2):
        # Params can be team objects or team names.
        # Creates a new matchup and adds it to the queue.
        if isinstance(team1, str):
            team1 = self.get_team(team1)
        if isinstance(team2, str):
            team2 = self.get_team(team2)
        self.add_matchup(Matchup(team1, team2))

    def add_matchup(self, matchup):
        # Adds a matchup to matchup queue.
        self.matchups.put(matchup)
        print("New matchup added:", matchup.team1.get_team_name(), "&", matchup.team2.get_team_name())

    def new_bracket(self):
        self.bracket = Bracket(self.matchups)

    # Evaluations
    def matchup_result(self, matchup, alg=None):
        # Default arg for alg is None.  Once we pick a default algorithm, it should
        # be that one
        winner = matchup.predictWinner(alg)
        return winner.get_team_name()
