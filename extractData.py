import pandas as pd


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

    print(rawBasic)
    print(rawAdv)

    # Test DF alterations
    """
    noCol = removeCol(rawBasic)
    print("Rank should be missing.")
    print(noCol)

    noHead = removeHeader(rawBasic)
    print("Header should be missing.")
    print(noHead)

    """
    #percentilesOfWiner = {}
    #get percentile of winner for each statistic
    #for i in basicHeaders:
    #    basicSchoolStatsDF[i].tolist()

if __name__ == "__main__":
    main()
