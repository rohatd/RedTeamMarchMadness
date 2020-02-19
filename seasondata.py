from team import Team

class SeasonData:

    def __init__(self, bas_df, adv_df=[], coach_df, year):
        self.basicData = bas_df
        self.advData = adv_df # Omitted for now
        self.coachData = coach_df
        self.teams = []
        self.year = year

    def initialize_teams(self):
        # TODO: Iterate through adv and basic data frames to fill
        # out team informations into Team objects, stored in
        # self.teams

        

        return 0
