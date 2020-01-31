import pandas as pd

def getHeaders(dataFile):
    fLine = dataFile.readline()
    headers = fLine.strip().split(",")
    fLine = dataFile.readline()
    headers2 = fLine.strip().split(",")
    
    for i in range(0,len(headers)):
        headers[i] = headers[i] + " " + headers2[i]
    return headers

def deleteHeaders(filename):
    for i in range(0,2):
        with open(filename, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(filename, 'w') as fout:
            fout.writelines(data[1:])

def loadData(headers,fileName):
    dataTable = pd.read_csv(fileName, 
                  sep=',', 
                  names=list(headers))
    return dataTable

def readFile(dataFile,fileName):
    headers = getHeaders(dataFile)
    deleteHeaders(fileName)
    return loadData(headers,fileName),headers

def main():

    year = 2019

    basicSchoolCSV = '{}basicdata.txt'.format(str(year))
    advSchoolCSV =  '{}advdata.txt'.format(str(year))

    #read 2019 basic school stats csv,return df with all info
    dataFile = open(basicSchoolCSV, 'r') 
    basicSchoolStatsDF,basicHeaders = readFile(dataFile,basicSchoolCSV)

    #read 2019 adv school stats csv,return df with all info
    dataFile = open(advSchoolCSV, 'r') 
    advSchoolStatsDF,advHeaders = readFile(dataFile,advSchoolCSV)


    print(basicSchoolStatsDF)
    print(advSchoolStatsDF)
    #percentilesOfWiner = {}
    #get percentile of winner for each statistic
    #for i in basicHeaders:
    #    basicSchoolStatsDF[i].tolist()

if __name__ == "__main__":
    main()