import pandas as pd
from seasondata import *

def parse_csv(filename):
    rawData = pd.read_csv(filename, header=[1])
    return rawData

# Functions to alter our initial raw dataframe, for any reason #######

def remove_col(dataframe, colName=""):
    # Remove the specified column, otherwise remove the first column in the dataframe
    res = dataframe.copy()
    if colName == "":
        res = res.drop(res.columns[[0]], axis=1)
        # res = res.drop(res.columns[[0]], axis=1, inplace=True)
    else:
        try:
            res = res.pop(colName)
        except:
            print("Error in remove_col(): Check spelling of column name.")
    return res

def remove_header(dataframe):
    # Reshapes the DF to remove the header strings.
    res = dataframe.copy()
    res.columns = range(res.shape[1])
    return res

def createSeasonData():
    # Creates a SeasonData object using 2018 - 2019 season data.
    # We can later take arguments that determine the specific season.

    # Read 2019 basic school stats csv, return DF with all info
    rawBasic = parse_csv("raw_basicschool_2018_2019.csv")
    # Read 2019 advanced school stats.
    rawAdv = parse_csv("raw_advschool_2018_2019.csv")
    rawCoaches = parse_csv("raw_coaches_2018_2019.csv")
    sd = SeasonData(2019, rawCoaches, rawBasic)
    return sd

def main():

    year = 2019

    # Dataframes with headers.  Indexing is not based on rank, as rank begins at 1.

    """
    print("BASIC DATA")
    print(rawBasic, "\nADVANCED DATA")
    print(rawAdv, "\nCOACH INFO")
    print(rawCoaches)
    """
    # Test DF alterations
    """
    noCol = remove_col(rawBasic)
    print("Rank should be missing.")
    print(noCol)
    noHead = remove_header(rawBasic)
    print("Header should be missing.")
    print(noHead)
    """
    # Test team initialization
    """
    print("\nTEAM INIT TEST:")
    teamRow = rawBasic.loc[0,:]
    teamName = teamRow['School']
    teamName = teamName[:-5]
    coachRow = rawCoaches.loc[rawCoaches['School'] == teamName]
    coach = rawCoaches.iat[0,0]
    # Verify school
    school = rawCoaches.iat[0,1]
    abilene = Team(2019, teamRow, coach)
    print("get_team_name():", abilene.get_team_name())
    print("get_coach():", abilene.get_coach())
    print("num_games():", abilene.num_games())
    print("num_wins():", abilene.num_wins())
    print("print_team_data():")
    abilene.print_team_data()
    """
    # SeasonData tests
    sdp = SeasonData(2018)
    sd = createSeasonData()
    akron = sd.get_team("Akron")
    print(akron.print_team_data())
    # Matchup integration tests
    sd.new_matchup("Akron", "Wyoming")
    xyMatch = Matchup(sd.get_team("Xavier"), sd.get_team("Yale"))
    sd.add_matchup(xyMatch)
    print(sd.matchup_result(xyMatch, "alg1"))

    #percentilesOfWiner = {}
    #get percentile of winner for each statistic
    #for i in basicHeaders:
    #    basicSchoolStatsDF[i].tolist()

if __name__ == "__main__":
    main()
