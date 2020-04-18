teamVocab = {  "Rk_x" : "Rank",
               "School" : "School",
               "G_x" : "Total Games",
               "W_x" : "Overall Wins",
               "L_x" : "Overall Losses",
               "W-L%_x" : "Win-Loss Percentage",
               "SRS_x" : "Simple Rating System",
               "SOS_x" : "Strength of Schedule",
               "W.1_x" : "Conference Wins",
               "L.1_x" : "Conference Losses",
               "W.2_x" : "Home Wins",
               "L.2_x" : "Home Losses",
               "W.3_x" : "Away Wins",
               "L.3_x" : "Away Losses",
               "Tm._x" : "Sum Team Points",
               "Opp._x" : "Sum Opponent Points",
               "MP_x" : "Minutes Played",
               "FG_x" : "Field Goals",
               "FGA_x" : "Field Goal Attempts",
               "FG%_x" : "Field Goal Percentage",
               "3P_x" : "3-Pointers Made",
               "3PA_x" : "3-Point Average",
               "3P%_x" : "3-Point Percentage",
               "FT_x" : "Free Throws",
               "FTA_x" : "Free Throw Attempts",
               "FT%_x" : "Free Throw Percentage",
               "ORB_x" : "Offensive Rebounds",
               "TRB_x" : "Total Rebounds",
               "AST_x" : "Assists",
               "STL_x" : "Steals",
               "BLK_x" : "Blocks",
               "TOV_x" : "Turnovers",
               "PF_x" : "Personal Fouls" }

coachVocab = { "Coach" : "Coach",
               "School" : "School",
               "Conference" : "Conference",
               "Since" : "School Career Start",
               "W.1" : "Current School Wins",
               "L.1" : "Current School Losses",
               "W-L%.1" : "Win-Loss Percentage",
               "NCAA" : "NCAA",
               "S16" : "S16",
               "FF" : "FF",
               "Chmp" : "Championships at Current School",
               "W.2" : "Career Overall Wins",
               "L.2" : "Career Overall Losses",
               "W-L%.1" : "Career Win-Loss Percentage",
               "NCAA.1" : "Career Overall NCAA",
               "S16.1" : "Overall S16",
               "FF.1" : "Overall FF",
               "Chmp.1" : "Total Career Championships"}

class Team:

    def __init__(self, year, team_data, coach_data):
        self.year = year
        # team_data is a row from our DF
        self.team_data = team_data
        self.coach_data = coach_data

    # Getters
    def get_team_name(self):
        return self.team_data['School']

    def get_year(self):
        return self.year

    def get_coach(self):
        return self.coach_data['Coach']

    def get_coach_data(self):
        return self.coach_data

    def num_games(self):
        return self.team_data['G_x']

    def num_wins(self, param="overall"):
        # Returns number of wins based on parameter.
        param = param.lower()
        res = -1
        if param == "overall":
            res = self.team_data['W_x']
        elif param == "conference":
            res = self.team_data['W.1_x']
        elif param == "home":
            res = self.team_data['W.2_x']
        elif param == "away":
            res = self.team_data['W.3_x']
        else:
            print("num_wins for", self.get_team_name, ": Invalid parameters.")
        return res

    def num_losses(self, param="overall"):
        # Returns number of losses based on parameter.
        param = param.lower()
        res = -1
        if param == "overall":
            res = self.team_data['L_x']
        elif param == "conference":
            res = self.team_data['L.1_x']
        elif param == "home":
            res = self.team_data['L.2_x']
        elif param == "away":
            res = self.team_data['L.3_x']
        else:
            print("num_losses for", self.get_team_name, ": Invalid parameters.")
        return res

    def get_attribute(self, param):
        # Argument 'param' should be a string of an attribute name.
        val = self.team_data[param]
        if isinstance(val, float):
            val = '%.3f'%(val)
        return str(val)

    def get_coach_attribute(self, param):
        val = self.coach_data[param]
        if isinstance(val, float):
            val = '%.3f'%(val)
        return str(val)

    def stats_json(self, response={}):
        # Constructs a dictionary to be converted into a JSON object to return to frontend (for Stats).
        # Should include coach info as well.
        def lookup(data, spec):
            if spec == "coach":
                vocab = coachVocab
            else:
                vocab = teamVocab
            try:
                for key in vocab:
                    print(key)
                    entry = vocab[key]
                    if spec == "coach":
                        res = self.get_coach_attribute(key)
                    else:
                        res = self.get_attribute(key)
                    if res == "nan":
                        res = "N/A"
                    data[entry] = res
            except:
                print("team.py: stats_json() ... Error looking up entries for", spec, "vocabulary")
                return None

        teamData = {}
        coachData = {}
        lookup(teamData, "team")
        lookup(coachData, "coach")
        response["Team"] = teamData
        response["Coach"] = coachData
        return response

    # Display functions
    def print_team_data(self):
        print(self.team_data)
