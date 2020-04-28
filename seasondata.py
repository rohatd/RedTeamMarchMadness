"""SeasonData Module

    creates a dataframe for each team in the NCAA per Season year
    main form of data extraction
"""
from queue import Queue
import pandas as pd
from team import Team
from matchup import Matchup
from bracket import *

class SeasonData:
    """SeasonData Class

    Attributes:
        teams (dict):   dictionary where team is key and data is value
        year (int): seaosn year
        matchups (queue):   queue of teams   
        bracket (list): bracket of matchups
    
    """
    def __init__(self, year, coach_file, basic_file, adv_file):
        """initialized dataframe"""

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
            # Iterate through adv and basic data frames to fill
            # out team informations into Team objects, stored in
            # self.teams
            merged_inner = pd.merge(left=bas_df, right=adv_df, left_on='School', right_on='School')
            num_teams = bas_df.shape[0]
            for i in range(num_teams):
                team_row = merged_inner.loc[i, :]
                team_name = team_row['School']
                # Trim 'NCAA' from the name
                if "NCAA" in team_name:
                    team_name = team_name[:-5]
                # Get coach data (single row corresponding to school name.)
                coach_row = coach_df.loc[coach_df['School'] == team_name].squeeze()
                self.teams[team_name] = Team(self.year, team_row, coach_row)



    # Getters
    def get_team(self, team_name):
        """Returns Team object"""
        return self.teams[team_name]

    def get_matchups(self):
        """Returns stored list of matchups, to be used however."""
        # Likely as init arg to form Bracket object.
        return self.matchups

    # Mutators (Add / Remove)
    def new_matchup(self, team1, team2):
        """creates and adds a matchup to queue
        
        args:
            team1 (str or team obj):    team1
            team2 (str or team obj):    team2
        """
        if isinstance(team1, str):
            team1 = self.get_team(team1)
        if isinstance(team2, str):
            team2 = self.get_team(team2)
        self.add_matchup(Matchup(team1, team2))

    def add_matchup(self, matchup):
        """Adds a matchup to matchup queue."""
        self.matchups.append(matchup)
        print("New matchup added:", matchup.team1.get_team_name(), "&", matchup.team2.get_team_name())

    def new_bracket(self):
        """creates new bracket"""
        self.bracket = Bracket(self.matchups)
