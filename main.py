#main file that calls classes to compute predicted bracket

from seasondata import *
import pandas as pd
from matchup import *
from sportsreference.ncaab.schedule import Schedule
from sportsreference.ncaab.teams import Teams
from itertools import product 


def init_seasondata():
    coach_file = "raw_coaches_2018_2019.csv"
    basic_file = "raw_basicschool_2018_2019.csv"
    adv_file = "raw_advschool_2018_2019.csv"

    sd = SeasonData(2019, coach_file, basic_file, adv_file)
    print("tester.py: SeasonData initialization successful.")
    return sd



def run():
	sd = init_seasondata()

	#gets top 64 team names in order and retrieves data from season data
	teamList = []
	file = open("64.txt", 'r')
	for team in file:
		teamName = sd.get_team(team.strip())
		teamList.append(teamName)

	#evaluates teams
	predictedBracket = Bracket(teamList)

	print("evaluating bracket")
	predictedBracket.evaluateBracket()

	print("getting bracket")
	predictedList = predictedBracket.getBracket()
	print(predictedList)

	# f = open("bracket.txt", "a")
	# for i in predictedList:
	# 	f.write(i + "\n")

	# f.close()



def main():
	run()


if __name__ == "__main__":
	main()