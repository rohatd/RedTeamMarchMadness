"""marchMadness Module

    connector of front end to backend
    extracts data using seasonData module

    Attributes:
        app (flask): flask app to run server
        SD (seasonData): seasonData dataframe
"""
import json
from flask import Flask, render_template, request, jsonify
from seasondata import *
from bracket import *
from collections import deque

app = Flask(__name__)
SD = None
B = None


# Request Handling
@app.route('/api/init/', methods=["GET", "POST"])
def init_sd():
    """initializes seasonData object"""
    # Stores SeasonData object in global var SD
    res = "SD load failure"
    global SD
    try:
        SD = SeasonData(2019, "raw_coaches_2018_2019.csv",
                        "raw_basicschool_2018_2019.csv", "raw_advschool_2018_2019.csv")
        res = "SD load success"
    except:
        print("handler.py: Something went wrong initializing SeasonData.")
    return res

# Individual page routes
@app.route("/")
@app.route("/home")
def home():
    """renders homepage"""
    return render_template('homepage.html')

@app.route("/team-compare")
def team_compare():
    """renders team compare page"""
    return render_template('teamCompare.html')

@app.route("/generate-bracket")
def generate_bracket():
    """renders generate bracket page"""

    teams = []
    file = open("bracket.txt", 'r')
    for line in file:
        teams.append(line.strip())
    # global B
    # try:
    #   B = Bracket(teamList)
    # except:
    #   print("bracket: something went wrong.")

    # teams = B.getBracket()
    #print(teams)
    return render_template('generateBracket.html', teams=teams)

@app.route("/stats")
def stats():
    """renders stats page"""
    return render_template('stats.html')


@app.route('/api/message/', methods=["POST"])
def main_interface():
    """team comparison query handler

    handlers inputted teams from user
    extracts stats for team and displays them

    return:
        response (json)
    """
    input = request.get_json()
    print("Message received:", input, type(input))

    # Formulate a fake response.  Somehow connect this to an actual
    # Team object request; look at architecture
    global SD
    team_name = input["message"]
    try:
        team = SD.get_team(team_name)
    except:
        return jsonify({"/api/message": "team name failed to load"})
    response = {}
    response["team"] = str(team_name)
    response["year"] = str(team.get_year())
    response["coach"] = str(team.get_coach())
    response["numGames"] = str(team.num_games())
    response["numWins"] = str(team.num_wins())
    response["numLosses"] = str(team.num_losses())

    response["homeWins"] = str(team.get_attribute("W.2_x"))
    response["awayWins"] = str(team.get_attribute("W.3_x"))
    response["rating"] = str(team.get_attribute("SRS_x"))
    response["w_l_p"] = str(team.get_attribute("W-L%_x"))
    return jsonify(response)

@app.route('/api/compare/', methods=["POST"])
def compare():
    """compares two teams based on stats

    return:
        response (json) 
    """
    input = request.get_json()
    print("Message received:", input, type(input))

    global SD
    t_1 = input["message1"]
    t_2 = input["message2"]
    team_name_1 = t_1[6:]
    team_name_2 = t_2[6:]

    try:
        team_1 = SD.get_team(team_name_1)
        team_2 = SD.get_team(team_name_2)

    except:
        return jsonify({"/api/compare": "team name failed to load"})
    response_1 = {}

    response_1["numWins"] = str(team_1.num_wins())
    response_1["homeWins"] = str(team_1.get_attribute("W.2_x"))
    response_1["awayWins"] = str(team_1.get_attribute("W.3_x"))
    response_1["rating"] = str(team_1.get_attribute("SRS_x"))
    response_1["w_l_p"] = str(team_1.get_attribute("W-L%_x"))

    response_1["numWins2"] = str(team_2.num_wins())
    response_1["homeWins2"] = str(team_2.get_attribute("W.2_x"))
    response_1["awayWins2"] = str(team_2.get_attribute("W.3_x"))
    response_1["rating2"] = str(team_2.get_attribute("SRS_x"))
    response_1["w_l_p2"] = str(team_2.get_attribute("W-L%_x"))


    response = {}
    if int(response_1["homeWins2"]) > int(response_1["homeWins"]):
        response["homeWins"] = team_name_2
    else:
        response["homeWins"] = team_name_1

    if int(response_1["awayWins2"]) > int(response_1["awayWins"]):
        response["awayWins"] = team_name_2
    else:
        response["awayWins"] = team_name_1

    if float(response_1["rating2"]) > float(response_1["rating"]):
        response["rating"] = team_name_2
    else:
        response["rating"] = team_name_1

    if float(response_1["w_l_p2"]) > float(response_1["w_l_p"]):
        response["w_l_p"] = team_name_2
    else:
        response["w_l_p"] = team_name_1


    print(response)
    return jsonify(response)



@app.route('/api/get-stats/', methods=["POST"])
def get_stats():
    """handles stats query
    
    retrieves stats for user inputted team
    Displays them to front end

    return:
        response (json)
    """
    input = request.get_json()
    query = input["query"]
    print("Stats query received:", input)
    """
    # Differentiate between a query for season, or team (TODO)
    if any(char.isdigit() for char in query):
        # If query contains digits, probably a season year query, e.g. "2019"

    else:
        """
    # Otherwise, a team name
    try:
        team = SD.get_team(query)
    except:
        return jsonify({"/api/get-stats": "Team name query failed to load."})
    return jsonify(team.stats_json())


@app.after_request
def add_headers(response):
    """handles response headers
    args:
        response: json

    returns:
        repsonse: json
    """
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


if __name__ == "__main__":
    """main program to run application"""
    app.run(debug=True)
