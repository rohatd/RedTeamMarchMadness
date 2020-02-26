from team import Team
from matchup import Matchup
from bracket import *
from extractData import *

class SeasonData:

    def __init__(self, year, coach_df=None, basic_df=None, adv_df=None):
        # Ensure arguments are in order Coach, Basic, Advanced.  All optional for init
        self.teams = {}
        self.year = year
        self.matchups = Queue()
        self.bracket = None  # Initial bracket is blank

        if (coach_df is not None) and (basic_df is not None):
            # If dataframes are passed, initialize teams.
            # TODO: accommodate adv_df
            self.initialize_teams(coach_df, basic_df)

    def initialize_teams(self, coach_df, basic_df, adv_df=None):
        # Iterate through adv and basic data frames to fill
        # out team informations into Team objects, stored in
        # self.teams
        numTeams = basic_df.shape[0]
        for i in range(numTeams):
            teamRow = basic_df.loc[i,:]
            teamName = teamRow['School']

            # Trim 'NCAA' from the name
            if "NCAA" in teamName:
                teamName = teamName[:-5]

            # Get coach info
            coachRow = coach_df.loc[coach_df['School'] == teamName]
            coachName = coachRow['Coach']
            try:
                coachName = coachName.tolist()[0]
            except:
                coachName = ""

            self.teams[teamName] = Team(self.year, teamRow, coachName)
        # TODO: accommodate advanced info dataframe by combining it with
        # teamRow created from basic dataframe.
        return 0

    # Getters
    def get_team(self, teamName):
        # Returns Team object
        return self.teams[teamName]

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
