from bracket import Bracket
from collections import deque

def main():
    teamList = deque()
    teamList.append('Stanford')
    teamList.append('UCLA')
    teamList.append('USC')
    teamList.append('Berkeley')
    print(teamList)
    #teamList = ['Stanford','UCLA', 'USC','Berkeley']
    testBracket = Bracket(teamList)
    testBracket.evaluateBracket()


if __name__ == "__main__":
    main()