# SeasonData Testing
from seasondata import *
import pandas as pd

def seasondata_test():
    coach_file = "raw_coaches_2018_2019.csv"
    basic_file = "raw_basicschool_2018_2019.csv"
    adv_file = "raw_advschool_2018_2019.csv"

    sd = SeasonData(2019, coach_file, basic_file, adv_file)
    print("tester.py: SeasonData initialization successful.")
    akron = sd.get_team("Akron")
    print("tester.py: get_team successful.")
    print(akron.team_data, isinstance(akron.team_data, pd.DataFrame))

    print(akron.get_coach(), isinstance(akron.get_coach(), pd.DataFrame))


def main():
    seasondata_test()

if __name__ == "__main__":
    main()