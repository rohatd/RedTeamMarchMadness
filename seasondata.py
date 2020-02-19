from team import Team

class SeasonData:

    def __init__(self, year, coach_df, bas_df):
        # Ensure arguments are in order Coach, Basic, Advanced.  All optional for init
        self.teams = {}
        self.year = year
#        self.matchups = []
        # if (coach_df is not None) and (bas_df is not None):
            # TODO: accommodate adv_df
        self.initialize_teams(coach_df, bas_df)

    def initialize_teams(self, coach_df, bas_df, adv_df=None):
        # Iterate through adv and basic data frames to fill
        # out team informations into Team objects, stored in
        # self.teams
        numTeams = bas_df.shape[0]
        for i in range(numTeams):
            teamRow = bas_df.loc[i,:]
            teamName = teamRow['School']
            # Trim 'NCAA' from the name
            if "NCAA" in teamName:
                teamName = teamName[:-5]
            coachRow = coach_df.loc[coach_df['School'] == teamName]
            coachName = coachRow['Coach']
            self.teams[teamName] = Team(self.year, teamRow, coachName)
        # TODO: accommodate advanced info dataframe by combining it with
        # teamRow created from basic dataframe.
        return 0

#    def form_matchup(team_a, team_b):
#        return 0

    def get_team(self, teamName):
        # Returns Team object
        return self.teams[teamName]
