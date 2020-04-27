import pandas as pd
from sportsreference.ncaab.schedule import Schedule
from sklearn.ensemble import RandomForestRegressor
import re
import random 
from multiprocessing import Process

# from scheduleData import *



class Matchup:

    def __init__(self,team1,team2):
        self.team1 = team1
        self.team2 = team2


    def get_winner(self):
        return RandomForestRegressor(2018)

    def get_regeressor_info(self,home,away):
        data = {'away_assist_percentage' : [away.get_attribute("AST%")],
                'away_assists' : [away.get_attribute('AST')],
                'away_block_percentage' : [away.get_attribute('BLK%')],
                'away_blocks' : [away.get_attribute('BLK')],
            #     'away_defensive_rebounds' : away.get_attribute('AST')],
                'away_effective_field_goal_percentage' : [away.get_attribute('eFG%')],
                'away_field_goal_attempts' : [away.get_attribute('FGA')],
                'away_field_goal_percentage' : [away.get_attribute('FG%')],
                'away_field_goals' : [away.get_attribute('FG')],
                'away_free_throw_attempt_rate' : [away.get_attribute('FTr')],
                'away_free_throw_attempts' : [away.get_attribute('FTA')],
                'away_free_throw_percentage' : [away.get_attribute('FT%')],
                'away_free_throws' : [away.get_attribute('FT')],
                'away_losses' : [away.get_attribute('L_x')],
                'away_minutes_played' : [away.get_attribute('MP')],
                'away_offensive_rating' : [away.get_attribute('ORtg')],
                'away_offensive_rebound_percentage' : [away.get_attribute('ORB%')],
                'away_offensive_rebounds' : [away.get_attribute('ORB')],
                'away_personal_fouls' : [away.get_attribute('PF')],
                'away_steal_percentage' : [away.get_attribute('STL%')],
                'away_steals' : [away.get_attribute('STL')],
                'away_three_point_attempt_rate' : [away.get_attribute('3PAr')],
                'away_three_point_field_goal_attempts' : [away.get_attribute('3PA')],
                'away_three_point_field_goal_percentage' : [away.get_attribute('3P%')],
                'away_three_point_field_goals' : [away.get_attribute('3P')],
                'away_total_rebound_percentage' : [away.get_attribute('TRB%')],
                'away_total_rebounds' : [away.get_attribute('TRB')],
                'away_true_shooting_percentage' : [away.get_attribute('TS%')],
                'away_turnover_percentage' : [away.get_attribute('TOV%')],
                'away_turnovers' : [away.get_attribute('TOV')],
                #'away_two_point_field_goal_attempts' : away.get_attribute('AST')],
                #'away_two_point_field_goal_percentage' : away.get_attribute('AST')],
                #'away_two_point_field_goals' : away.get_attribute('AST')],
                'away_win_percentage' : [away.get_attribute('W-L%_x')],
                'away_wins' : [away.get_attribute('W_x')],
                'home_assist_percentage' : [home.get_attribute("AST%")],
                'home_assists' : [home.get_attribute('AST')],
                'home_block_percentage' : [home.get_attribute('BLK%')],
                'home_blocks' : [home.get_attribute('BLK')],
            #     'home_defensive_rebounds' : home.get_attribute('AST')],
                'home_effective_field_goal_percentage' : [home.get_attribute('eFG%')],
                'home_field_goal_attempts' : [home.get_attribute('FGA')],
                'home_field_goal_percentage' : [home.get_attribute('FG%')],
                'home_field_goals' : [home.get_attribute('FG')],
                'home_free_throw_attempt_rate' : [home.get_attribute('FTr')],
                'home_free_throw_attempts' : [home.get_attribute('FTA')],
                'home_free_throw_percentage' : [home.get_attribute('FT%')],
                'home_free_throws' : [home.get_attribute('FT')],
                'home_losses' : [home.get_attribute('L_x')],
                'home_minutes_played' : [home.get_attribute('MP')],
                'home_offensive_rating' : [home.get_attribute('ORtg')],
                'home_offensive_rebound_percentage' : [home.get_attribute('ORB%')],
                'home_offensive_rebounds' : [home.get_attribute('ORB')],
                'home_personal_fouls' : [home.get_attribute('PF')],
                'home_steal_percentage' : [home.get_attribute('STL%')],
                'home_steals' : [home.get_attribute('STL')],
                'home_three_point_attempt_rate' : [home.get_attribute('3PAr')],
                'home_three_point_field_goal_attempts' : [home.get_attribute('3PA')],
                'home_three_point_field_goal_percentage' : [home.get_attribute('3P%')],
                'home_three_point_field_goals' : [home.get_attribute('3P')],
                'home_total_rebound_percentage' : [home.get_attribute('TRB%')],
                'home_total_rebounds' : [home.get_attribute('TRB')],
                'home_true_shooting_percentage' : [home.get_attribute('TS%')],
                'home_turnover_percentage' : [home.get_attribute('TOV%')],
                'home_turnovers' : [home.get_attribute('TOV')],
                #'home_two_point_field_goal_attempts' : home.get_attribute('AST'),
                #'home_two_point_field_goal_percentage' : home.get_attribute('AST'),
                #'home_two_point_field_goals' : home.get_attribute('AST'),
                'home_win_percentage' : [home.get_attribute('W-L%_x')],
                'home_wins' : [home.get_attribute('W_x')]
                }
        return pd.DataFrame(data)

    # def init_scheduleData(self):
    #     box_file = "data.csv"
    #     bs = ScheduleData(2019, box_file)
    #     print("tester.py: ScheduleData initialization successful.")
    #     return bs

    def random_forest_regressor(self,year):
        #print("in random forest regressor")
        #fields brought in by sports reference api that we don't want
        FIELDS_TO_DROP = ['away_points', 'home_points', 'date', 'location',
                  'losing_abbr', 'losing_name', 'winner', 'winning_abbr',
                  'winning_name', 'home_ranking', 'away_ranking', 'away_defensive_rebounds',
                  'home_defensive_rebounds', 'away_two_point_field_goal_attempts', 'away_two_point_field_goal_percentage', 'away_two_point_field_goals'
                  ,'home_two_point_field_goal_attempts', 'home_two_point_field_goal_percentage','home_two_point_field_goals','pace','away_defensive_rating', 'away_defensive_rebound_percentage','home_defensive_rating','home_defensive_rebound_percentage']
        

        #pull in the scores for all games played in a certain season for both teams
        team1_name = self.team1.get_team_name().replace(" NCAA", "").replace(" ", "-").replace("(", "").replace(")", "").replace("'", "")
        team2_name = self.team2.get_team_name().replace(" NCAA", "").replace(" ", "-").replace("(", "").replace(")", "").replace("'", "")
        if team1_name == "UC-Irvine":
            team1_name = "CALIFORNIA-IRVINE"
        if team2_name == "UC-Irvine":
            team2_name = "CALIFORNIA-IRVINE"

        team1_schedule = Schedule(team1_name,year)
        team2_schedule = Schedule(team2_name,year)
        #team1_schedule.dataframe_extended.to_excel(r'C:\Users\dr171\OneDrive\Documents\College\Spring2020\sd&d\RedTeamMarchMadness\team1_schedule.xlsx', index=True)
        print("got schedules")

        team1_df = team1_schedule.dataframe_extended
        print(team1_df.head())
        team1_df_home = team1_df[team1_df.index.str.contains(self.team1.get_team_name().replace(" NCAA","").replace(" ","-").lower())]
        team1_df_away = team1_df[~team1_df.index.str.contains(self.team1.get_team_name().replace(" NCAA","").replace(" ","-").lower())]

        team2_df = team2_schedule.dataframe_extended
        print(team2_df.head())
        team2_df_home = team2_df[team2_df.index.str.contains(self.team2.get_team_name().replace(" NCAA","").replace(" ","-").lower())]
        team2_df_away = team2_df[~team2_df.index.str.contains(self.team2.get_team_name().replace(" NCAA","").replace(" ","-").lower())]

        # box_file = "data.csv"
        # bs = ScheduleData(2019, box_file)
        # print("tester.py: ScheduleData initialization successful.")
        # data_bf = bs.box_df
        # print("Initialized data")

        # team1_df_home = data_bf[data_bf.iloc[:,0].str.contains(self.team1.get_team_name().replace(" NCAA","").replace(" ","-").lower())]
        # team1_df_away = data_bf[~data_bf.iloc[:,0].str.contains(self.team1.get_team_name().replace(" NCAA","").replace(" ","-").lower())]

        # #print(team1_df_home)

        # team2_df_home = data_bf[data_bf.iloc[:,0].str.contains(self.team2.get_team_name().replace(" NCAA","").replace(" ","-").lower())]
        # team2_df_away = data_bf[~data_bf.iloc[:,0].str.contains(self.team2.get_team_name().replace(" NCAA","").replace(" ","-").lower())]
        
        print("seperated home and away")
        #compile into one dataset
        dataset_1 = pd.concat([team1_df_home, team2_df_away])
        dataset_2 = pd.concat([team2_df_home, team1_df_away])
        
        # dataset_1.drop(dataset_1.columns[[0]], axis=1, inplace=True)
        # dataset_2.drop(dataset_2.columns[[0]], axis=1, inplace=True)
        print('concated proper dataframes')
        #create training sets from datasetf
        X_train_1 = dataset_1.drop(FIELDS_TO_DROP, 1).dropna().drop_duplicates()
        X_train_2 = dataset_2.drop(FIELDS_TO_DROP, 1).dropna().drop_duplicates()


        print(X_train_1)
        print(X_train_2)

        Y_train_1 = dataset_1[['home_points','away_points']]
        Y_train_2 = dataset_2[['home_points','away_points']]

        print(Y_train_1)
        print(Y_train_2)

        print('created training sets')
        #pd.DataFrame(X_train).to_excel(r'C:\Users\dr171\OneDrive\Documents\College\Spring2020\sd&d\RedTeamMarchMadness\X_train.xlsx', index=False)
        #pd.DataFrame(Y_train).to_excel(r'C:\Users\dr171\OneDrive\Documents\College\Spring2020\sd&d\RedTeamMarchMadness\Y_train.xlsx', index=False)

        while(len(X_train_1) != len(Y_train_1)):
            Y_train_1 = Y_train_1[:-1]

        while(len(X_train_2) != len(Y_train_2)):
            Y_train_2 = Y_train_2[:-1]
        

        #create the x test (need to create method)
        X_test_1  = self.get_regeressor_info(self.team1,self.team2)#team1.get_attributes() + team2.get_attributes
        X_test_2  = self.get_regeressor_info(self.team2,self.team1)#team1.get_attributes() + team2.get_attributes

        print('got test sets')
        #pd.DataFrame(X_train).to_excel(r'C:\Users\dr171\OneDrive\Documents\College\Spring2020\sd&d\RedTeamMarchMadness\X_train_{0}.xlsx'.format(self.team1.get_team_name()))
        #pd.DataFrame(X_test).to_excel(r'C:\Users\dr171\OneDrive\Documents\College\Spring2020\sd&d\RedTeamMarchMadness\X_test_{0}.xlsx'.format(self.team1.get_team_name()))
        #print(X_train)
        #print(X_test)
        #parameters for model (could use tweaking to improve accuracy in the future)

        parameters = {
            'bootstrap': True,
            'max_depth': 6,
            'max_features': None,
            'min_samples_leaf': 50,
            'min_samples_split': 12,
            'n_estimators': 100}
        #create model
        model_1 = RandomForestRegressor(**parameters)
        model_2 = RandomForestRegressor(**parameters)

        # print('started threading')
        # p1 = Process(target=model_1.fit,args = (X_train_1,Y_train_1,))
        # p1.start()
        # p2 = Process(target=model_2.fit,args = (X_train_2,Y_train_2,))
        # p2.start()
        # p1.join()
        # p2.join()
        print('finished join')

        model_1.fit(X_train_1, Y_train_1)
        model_2.fit(X_train_2, Y_train_2)

        #predict outcome of game based of season statistics for both teams
        spread_1 = model_1.predict(X_test_1).astype(int)
        spread_2 = model_2.predict(X_test_2).astype(int)

        print('predicted spreads')
        spread_1 = str(spread_1[0]).replace("[","").replace("]","").split(" ")
        spread_2 = str(spread_2[0]).replace("[","").replace("]","").split(" ")
        
        team1_score = int(spread_1[0]) + int(spread_2[1])
        team2_score = int(spread_1[1]) + int(spread_2[0])

        print("Team 1 score" , team1_score, self.team1.get_team_name())
        print("Team 2 score", team2_score, self.team2.get_team_name())


        if(team1_score>team2_score):
                return self.team1
        if(team1_score<team2_score):
               return self.team2
        if(team1_score == team2_score):
                return random.choice([self.team1,self.team2])
        
        
        # if(spread[0] >spread[1]):
        #     return self.team2.get_team_name().replace(" NCAA","")
        # elif( spread[1]> spread[0]):
        #     return self.team1.get_team_name().replace(" NCAA","")
        # else:
        #     return self.team1.get_team_name().replace(" NCAA","")
        

    

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

    def predict_winner(self, alg=None):
        # Sample alg
        alg = alg.lower()
        if alg == "alg1":
            return self.alg1()
        # ... Add more alg conditions here perhaps

        else:
            return self.getWinner()