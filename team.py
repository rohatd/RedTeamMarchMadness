

class Team:

    def __init__(self, year, team_data, coach):
        self.year = year
        # team_data is a row from our DF
        self.team_data = team_data
        self.coach = coach

    # Getters
    def get_team_name(self):
        return self.team_data['School']

    def get_year(self):
        return self.year

    def get_coach(self):
        return self.coach

    def num_games(self):
        return self.team_data['G']

    def num_wins(self, param="overall"):
        # Returns number of wins based on parameter.
        param = param.lower()
        res = -1
        if param == "overall":
            res = self.team_data['W']
        elif param == "conference":
            res = self.team_data['W.1']
        elif param == "home":
            res = self.team_data['W.2']
        elif param == "away":
            res = self.team_data['W.3']
        else:
            print("num_wins for", self.get_team_name, ": Invalid parameters.")
        return res

    def num_losses(self, param="overall"):
        # Returns number of losses based on parameter.
        param = param.lower()
        res = -1
        if param == "overall":
            res = self.team_data['L']
        elif param == "conference":
            res = self.team_data['L.1']
        elif param == "home":
            res = self.team_data['L.2']
        elif param == "away":
            res = self.team_data['L.3']
        else:
            print("num_losses for", self.get_team_name, ": Invalid parameters.")
        return res

    def get_attribute(self, param):
        # Argument 'param' should be a string of an attribute name.
        return self.team_data[param]

    # Display functions
    def print_team_data(self):
        print(self.team_data)
        return 0

    
