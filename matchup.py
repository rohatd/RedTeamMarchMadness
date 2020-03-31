import pandas as pd
from sportsreference.ncaab.schedule import Schedule
from sklearn.ensemble import RandomForestRegressor



class Matchup:

    def __init__(self,team1,team2):
        self.team1 = team1
        self.team2 = team2


    def getWinner(self):
        return RandomForestRegressor(2018)


    def randomForestRegressor(self,year):
        '''
        Things to do still:
            -Implement X_test information method
        '''
        #fields brought in by sports reference api that we don't want
        FIELDS_TO_DROP = ['away_points', 'home_points', 'date', 'location',
                  'losing_abbr', 'losing_name', 'winner', 'winning_abbr',
                  'winning_name', 'home_ranking', 'away_ranking', 'away_defensive_rebounds', 
                  'home_defensive_rebounds', 'away_two_point_field_goal_attempts', 'away_two_point_field_goal_percentage', 'away_two_point_field_goals'
                  ,'home_two_point_field_goal_attempts', 'home_two_point_field_goal_percentage','home_two_point_field_goals','pace']

        #pull in the scores for all games played in a certain season for both teams
        team1_schedule = Schedule(team1.get_team_name(),year)
        team2_schedule = Schedule(team2.get_team_name(),year)
        
        #compile into one dataset
        dataset = pd.concat([team1_schedule.dataframe_extended, team2_schedule.dataframe_extended])
        
        #create training sets from dataset
        X_train = dataset.drop(FIELDS_TO_DROP, 1).dropna().drop_duplicates()
        Y_train = dataset[['home_points', 'away_points']].values
        
        #create the x test (need to create method)
        X_test  = get_regeressor_info(team1,team2)#team1.get_attributes() + team2.get_attributes
        
        #parameters for model (could use tweaking to improve accuracy in the future)
        parameters = {'bootstrap': False,
                    'min_samples_leaf': 3,
                    'n_estimators': 50,
                    'min_samples_split': 10,
                    'max_features': 'sqrt',
                    'max_depth': 6}
        #create model
        model = RandomForestRegressor(**parameters)
        #train model using the season data
        model.fit(X_train, y_train)
        
        #predict outcome of game based of season statistics for both teams
        print(model.predict(X_test).astype(int))
        
    def get_regressor_info(team1,team2):
        data = {'away_assist_percentage' : team2.get_attribute('AST%'), 
                'away_assists' : team2.get_attribute('AST'),
                'away_block_percentage' : team2.get_attribute('BLK%'),
                'away_blocks' : team2.get_attribute('BLK'),
           #     'away_defensive_rebounds' : team2.get_attribute('AST'),
                'away_effective_field_goal_percentage' : team2.get_attribute('eFG%'), 
                'away_field_goal_attempts' : team2.get_attribute('FGA'), 
                'away_field_goal_percentage' : team2.get_attribute('FG%'),
                'away_field_goals' : team2.get_attribute('FG'),
                'away_free_throw_attempt_rate' : team2.get_attribute('FTr'), 
                'away_free_throw_attempts' : team2.get_attribute('FTA'), 
                'away_free_throw_percentage' : team2.get_attribute('FT%'),
                'away_free_throws' : team2.get_attribute('FT'),
                'away_losses' : team2.get_attribute('L'), 
                'away_minutes_played' : team2.get_attribute('MP'), 
                'away_offensive_rating' : team2.get_attribute('ORtg'),
                'away_offensive_rebound_percentage' : team2.get_attribute('ORB%'),
                'away_offensive_rebounds' : team2.get_attribute('ORB'), 
                'away_personal_fouls' : team2.get_attribute('PF'), 
                'away_steal_percentage' : team2.get_attribute('STL%'),
                'away_steals' : team2.get_attribute('STL'),
                'away_three_point_attempt_rate' : team2.get_attribute('3PAr'), 
                'away_three_point_field_goal_attempts' : team2.get_attribute('3PA'), 
                'away_three_point_field_goal_percentage' : team2.get_attribute('3P%'),
                'away_three_point_field_goals' : team2.get_attribute('3P'),
                'away_total_rebound_percentage' : team2.get_attribute('TRB%'),
                'away_total_rebounds' : team2.get_attribute('TRB'),
                'away_true_shooting_percentage' : team2.get_attribute('TS%'), 
                'away_turnover_percentage' : team2.get_attribute('TOV%'), 
                'away_turnovers' : team2.get_attribute('TOV'),
                #'away_two_point_field_goal_attempts' : team2.get_attribute('AST'),
                #'away_two_point_field_goal_percentage' : team2.get_attribute('AST'), 
                #'away_two_point_field_goals' : team2.get_attribute('AST'), 
                'away_win_percentage' : team2.get_attribute('W-L%'),
                'away_wins' : team2.get_attribute('W'),
                'home_assist_percentage' : team1.get_attribute('AST%'), 
                'home_assists' : team1.get_attribute('AST'),
                'home_block_percentage' : team1.get_attribute('BLK%'),
                'home_blocks' : team1.get_attribute('BLK'),
           #     'home_defensive_rebounds' : team1.get_attribute('AST'),
                'home_effective_field_goal_percentage' : team1.get_attribute('eFG%'), 
                'home_field_goal_attempts' : team1.get_attribute('FGA'), 
                'home_field_goal_percentage' : team1.get_attribute('FG%'),
                'home_field_goals' : team1.get_attribute('FG'),
                'home_free_throw_attempt_rate' : team1.get_attribute('FTr'), 
                'home_free_throw_attempts' : team1.get_attribute('FTA'), 
                'home_free_throw_percentage' : team1.get_attribute('FT%'),
                'home_free_throws' : team1.get_attribute('FT'),
                'home_losses' : team1.get_attribute('L'), 
                'home_minutes_played' : team1.get_attribute('MP'), 
                'home_offensive_rating' : team1.get_attribute('ORtg'),
                'home_offensive_rebound_percentage' : team1.get_attribute('ORB%'),
                'home_offensive_rebounds' : team1.get_attribute('ORB'), 
                'home_personal_fouls' : team1.get_attribute('PF'), 
                'home_steal_percentage' : team1.get_attribute('STL%'),
                'home_steals' : team1.get_attribute('STL'),
                'home_three_point_attempt_rate' : team1.get_attribute('3PAr'), 
                'home_three_point_field_goal_attempts' : team1.get_attribute('3PA'), 
                'home_three_point_field_goal_percentage' : team1.get_attribute('3P%'),
                'home_three_point_field_goals' : team1.get_attribute('3P'),
                'home_total_rebound_percentage' : team1.get_attribute('TRB%'),
                'home_total_rebounds' : team1.get_attribute('TRB'),
                'home_true_shooting_percentage' : team1.get_attribute('TS%'), 
                'home_turnover_percentage' : team1.get_attribute('TOV%'), 
                'home_turnovers' : team1.get_attribute('TOV'),
                #'home_two_point_field_goal_attempts' : team1.get_attribute('AST'),
                #'home_two_point_field_goal_percentage' : team1.get_attribute('AST'), 
                #'home_two_point_field_goals' : team1.get_attribute('AST'), 
                'home_win_percentage' : team1.get_attribute('W-L%'),
                'home_wins' : team1.get_attribute('W')
                }
            return pd.DataFrame(data, index=[0])

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
