import pandas as pd
from team import Team

def parseCSV(filename):
    rawData = pd.read_csv(filename, header=[1])
    return rawData

# Functions to alter our initial raw dataframe, for any reason #######

def removeCol(dataframe, colName=""):
    # Remove the specified column, otherwise remove the first column in the dataframe
    res = dataframe.copy()
    if colName == "":
        res = res.drop(res.columns[[0]], axis=1)
        # res = res.drop(res.columns[[0]], axis=1, inplace=True)
    else:
        try:
            res = res.pop(colName)
        except:
            print("Error in removeCol(): Check spelling of column name.")
    return res

def removeHeader(dataframe):
    # Reshapes the DF to remove the header strings.
    res = dataframe.copy()
    res.columns = range(res.shape[1])
    return res



def main():

    year = 2019

    # Dataframes with headers.  Indexing is not based on rank, as rank begins at 1.

    # Read 2019 basic school stats csv, return DF with all info
    rawBasic = parseCSV("raw_basicschool_2018_2019.csv")
    # Read 2019 advanced school stats.
    rawAdv = parseCSV("raw_advschool_2018_2019.csv")
    rawCoaches = parseCSV("raw_coaches_2018_2019.csv")

    """
    print("BASIC DATA")
    print(rawBasic, "\nADVANCED DATA")
    print(rawAdv, "\nCOACH INFO")
    print(rawCoaches)
    """
    # Test DF alterations
    """
    noCol = removeCol(rawBasic)
    print("Rank should be missing.")
    print(noCol)

    noHead = removeHeader(rawBasic)
    print("Header should be missing.")
    print(noHead)
    """
    # Test team initialization
    """
    print("\nTEAM INIT TEST:")
    teamRow = rawBasic.loc[0,:]
    a = teamRow['School']
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
    
    #percentilesOfWiner = {}
    #get percentile of winner for each statistic
    #for i in basicHeaders:
    #    basicSchoolStatsDF[i].tolist()

if __name__ == "__main__":
    main()
