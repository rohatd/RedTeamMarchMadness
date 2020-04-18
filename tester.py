# SeasonData Testing
from seasondata import *
import pandas as pd
from matchup import *
from sportsreference.ncaab.schedule import Schedule
from sportsreference.ncaab.teams import Teams
from itertools import product

def seasondata_test():
    coach_file = "raw_coaches_2018_2019.csv"
    basic_file = "raw_basicschool_2018_2019.csv"
    adv_file = "raw_advschool_2018_2019.csv"

    sd = SeasonData(2019, coach_file, basic_file, adv_file)
    print("tester.py: SeasonData initialization successful.")
    akron = sd.get_team("Akron")
    print("tester.py: get_team successful.")
    print(akron.stats_json())



def test():

    coach_file = "raw_coaches_2018_2019.csv"
    basic_file = "raw_basicschool_2018_2019.csv"
    adv_file = "raw_advschool_2018_2019.csv"


    #successfully intialize season data
    sd = SeasonData(2019, coach_file, basic_file, adv_file)
    print("tester.py: SeasonData initialization successful.")


    #successfully get teams
    TexasTech = sd.get_team("Texas Tech")
    MichiganSt = sd.get_team("Michigan State")
    Virginia = sd.get_team("Virginia")
    Duke = sd.get_team("Duke")
    Auburn = sd.get_team("Auburn")
    Kentucky = sd.get_team("Kentucky")
    Gonzaga = sd.get_team("Gonzaga")
    Purdue = sd.get_team("Purdue")
    FloridaState = sd.get_team("Florida State")
    Michigan = sd.get_team("Michigan")
    LSU = sd.get_team("Louisiana State")
    VirginiaTech = sd.get_team("Virginia Tech")
    UNC = sd.get_team("North Carolina")
    Houston = sd.get_team("Houston")
    Tennessee = sd.get_team("Tennessee")
    Oregon = sd.get_team("Oregon")

    #Oregon.print_team_data()

    teamList = []
    teamList.append(FloridaState)
    teamList.append(Gonzaga)
    teamList.append(TexasTech)
    teamList.append(Michigan)

    
    #test create bracket 
    testBracket = Bracket(teamList)
    
    #test evaluate bracket
    testBracket.evaluateBracket()

    #test return list of front end bracket input
    #print(testBracket.getBracket())


    #param_grid = {
    #'bootstrap': [True, False],
    #'max_depth': [6,150],
    #'max_features': [None,50],
    #'min_samples_leaf': [3,110],
    #'min_samples_split': [8, 12],
    #'n_estimators': [100, 1000]
    #}


    # i = {
    # 'bootstrap': True,
    # 'max_depth': 6,
    # 'max_features': None,
    # 'min_samples_leaf': 50,
    # 'min_samples_split': 12,
    # 'n_estimators': 100
    # }

    #create teamList to insert into Bracket
    
    # teamList.append(LSU)
    # teamList.append(MichiganSt)
    # teamList.append(VirginiaTech)
    # teamList.append(Duke)
    # teamList.append(Auburn)
    # teamList.append(UNC)
    # teamList.append(Houston)
    # teamList.append(Kentucky)
    # teamList.append(Purdue)
    # teamList.append(Tennessee)
    # teamList.append(Oregon)
    # teamList.append(Virginia)

    # while len(teamList) != 1:
    #     t1 = teamList.pop(0)
    #     t2 = teamList.pop(0)
    #     teamList.append(t1)
    # print(teamList[0].get_team_name())


    #print(Schedule("Duke",2019).dataframe_extended)

    #correct_combo = 0 

    # matchup_list = [(Purdue,Tennessee)]

    # for param in product(*param_grid.values()):
    #     winners = []
    #     for i in matchup_list:
            
    #         team0score=0
    #         team1score=0
    #         testMatchup = Matchup(i[0],i[1])
    #         spread = testMatchup.randomForestRegressor(2019,param)

    #         testMatchup = Matchup(i[1],i[0])
    #         spread2 = testMatchup.randomForestRegressor(2019,param)
            
    #         spread = str(spread[0]).replace("[","").replace("]","").split(" ")
    #         spread2 = str(spread2[0]).replace("[","").replace("]","").split(" ")
            
    #         team0score = int(spread[0]) + int(spread2[1])
    #         team1score = int(spread[1]) + int(spread2[0])

    #         print("{0} : {1}".format(i[0].get_team_name(),team0score))
    #         print("{0} : {1}".format(i[1].get_team_name(),team1score))

    #         if(team0score>team1score):
    #             winners.append(i[0].get_team_name())
    #         if(team0score<team1score):
    #             winners.append(i[1].get_team_name())
    #         if(team0score == team1score):
    #             winners.append(i[0].get_team_name())
    #             winners.append(i[1].get_team_name())
    #         print()
    #         print()
    #         print()
    #     print(param)
    #     print(winners)

        
        
        #correct = 0
        #print('Sweet Sixteen')
        
    #testMatchup = Matchup(FloridaState,Gonzaga)
    #print(testMatchup.randomForestRegressor(2019,i))

    #testMatchup = Matchup(Gonzaga,FloridaState)
    #print(testMatchup.randomForestRegressor(2019,i))

    #testMatchup = Matchup(Tennessee,Purdue)
    #print(testMatchup.randomForestRegressor(2019,i))

    #testMatchup = Matchup(Purdue, Tennessee)
    #print(testMatchup.randomForestRegressor(2019,i))

    #testMatchup = Matchup(Auburn,UNC)
    #print(testMatchup.randomForestRegressor(2019,i))

    # testMatchup = Matchup(UNC,Auburn)
    # print(testMatchup.randomForestRegressor(2019,i))

    # testMatchup = Matchup(LSU,MichiganSt)
    # print(testMatchup.randomForestRegressor(2019,i))
    
    # testMatchup = Matchup(MichiganSt,LSU)
    # print(testMatchup.randomForestRegressor(2019,i))

    # testMatchup = Matchup(TexasTech,Michigan)
    # print(testMatchup.randomForestRegressor(2019,i))
    
    # testMatchup = Matchup(Michigan,TexasTech)
    # print(testMatchup.randomForestRegressor(2019,i))

    # testMatchup = Matchup(Virginia,Oregon)
    # print(testMatchup.randomForestRegressor(2019,i))

    # testMatchup = Matchup(Oregon,Virginia)
    # print(testMatchup.randomForestRegressor(2019,i))

    # testMatchup = Matchup(Houston,Kentucky)
    # print(testMatchup.randomForestRegressor(2019,i))

    # testMatchup = Matchup(Kentucky,Houston)
    # print(testMatchup.randomForestRegressor(2019,i))

    # testMatchup = Matchup(Duke,VirginiaTech)
    # print(testMatchup.randomForestRegressor(2019,i))

    # testMatchup = Matchup(VirginiaTech,Duke)
    # print(testMatchup.randomForestRegressor(2019,i))

#        if(testMatchup.randomForestRegressor(2019,i) == 'Gonzaga'):
 #           correct+=1

        # testMatchup = Matchup(Tennessee,Purdue)
        # if(testMatchup.randomForestRegressor(2019,i) == 'Purdue'):
        #     correct+=1

        # testMatchup = Matchup(Auburn,UNC)
        # if(testMatchup.randomForestRegressor(2019,i) == 'Auburn'):
        #     correct+=1

        # testMatchup = Matchup(LSU,MichiganSt)
        # if(testMatchup.randomForestRegressor(2019,i) == 'Michigan State'):
        #     correct+=1

        # testMatchup = Matchup(TexasTech,Michigan)
        # if(testMatchup.randomForestRegressor(2019,i) == 'Texas Tech'):
        #     correct+=1

        # testMatchup = Matchup(Virginia,Oregon)
        # if(testMatchup.randomForestRegressor(2019,i) == 'Virginia'):
        #     correct+=1

        # testMatchup = Matchup(Houston,Kentucky)
        # if(testMatchup.randomForestRegressor(2019,i) == 'Kentucky'):
        #     correct+=1

        # testMatchup = Matchup(Duke,VirginiaTech)
        # if(testMatchup.randomForestRegressor(2019,i) == 'Duke'):
        #     correct+=1

        # print('Elite Eight')
        # testMatchup = Matchup(TexasTech,Gonzaga)
        # if(testMatchup.randomForestRegressor(2019,i) == 'Texas Tech'):
        #     correct+=1

        # testMatchup = Matchup(Virginia,Purdue)
        # if(testMatchup.randomForestRegressor(2019,i) == 'Virginia'):
        #     correct+=1

        # testMatchup = Matchup(Auburn,Kentucky)
        # if(testMatchup.randomForestRegressor(2019,i) == 'Auburn'):
        #     correct+=1

        # testMatchup = Matchup(Duke,MichiganSt)
        # if(testMatchup.randomForestRegressor(2019,i) == 'Michigan State'):
        #     correct+=1

        # if((correct/12) > accuracy):
        #     accuracy = correct/12
        #     correct_combo = i


    #print(correct_combo)
    #print(accuracy)



def main():
    #seasondata_test()
    test()
    

    

if __name__ == "__main__":
    main()
