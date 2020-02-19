
class Matchup:

    def __init__(self,team1,team2):
        self.team1 = team1
        self.team2 = team2


    def getWinner(self):
        return self.team1


    def alg1(self):
        # Sample alg, compares W-L percentages
        team1WL = self.team1.get_attribute('W-L%')
        team2WL = self.team2.get_attribute('W-L%')
        print("Alg1: Win / Loss Percentage.")
        print(self.team1.get_team_name(), ":", team1WL)
        print(self.team2.get_team_name(), ":", team2WL)
        if team1WL >= team2WL:
            return self.team1
        else:
            return self.team2

    def predictWinner(self, alg=None):
        # Sample alg
        alg = alg.lower()
        if alg == "alg1":
            return self.alg1()
        # ... Add more alg conditions here perhaps

        else:
            return self.getWinner()
