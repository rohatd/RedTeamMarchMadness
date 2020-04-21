from sportsreference.ncaab.schedule import Schedule
import pandas as pd
from sportsreference.ncaab.teams import Teams

for team in Teams():
    if(team.name == 'Duke'):
        print(team.defe)