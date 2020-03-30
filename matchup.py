
class Matchup:

    def __init__(self,team1,team2):
        self.team1 = team1
        self.team2 = team2


    def getWinner(self):
        return self.team1
    
    def randomForestRegressor(self,year):
        '''
        Things to do still:
            -Implement X_test information method
        '''
        #fields brought in by sports reference api that we don't want
        FIELDS_TO_DROP = ['away_points', 'home_points', 'date', 'location',
                  'losing_abbr', 'losing_name', 'winner', 'winning_abbr',
                  'winning_name', 'home_ranking', 'away_ranking']

        #pull in the scores for all games played in a certain season for both teams
        team1_schedule = Schedule(team1.get_team_name(),year)
        team2_schedule = Schedule(team2.get_team_name(),year)
        
        #compile into one dataset
        dataset = pd.concat([team1_schedule.dataframe_extended, team2_schedule.dataframe_extended])
        
        #create training sets from dataset
        X_train = dataset.drop(FIELDS_TO_DROP, 1).dropna().drop_duplicates()
        Y_train = dataset[['home_points', 'away_points']].values
        
        #create the x test (need to create method)
        X_test  = team1.get_attributes() + team2.get_attributes
        
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
