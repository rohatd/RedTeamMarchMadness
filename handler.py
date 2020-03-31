# Flask message handler
# Make sure you export the flask path: "$ export FLASK_APP=handler.py"
# Reference: https://medium.com/@gokhang1327/separate-front-end-from-back-end-with-flask-ajax-a5b22b12d001
from flask import Flask, request, jsonify, make_response
from seasondata import *
import json

app = Flask(__name__)
SD = None

@app.route('/api/init/', methods=["GET", "POST"])
def init_sd():
    # Stores SeasonData object in global var SD
    res = "SD load failure"
    global SD
    try:
        SD = SeasonData(2019, "raw_coaches_2018_2019.csv", "raw_basicschool_2018_2019.csv", "raw_advschool_2018_2019.csv")
        res = "SD load success"
    except:
        print("handler.py: Something went wrong initializing SeasonData.")
    return res

@app.route('/api/message/', methods=["POST"])
def main_interface():
    input = request.get_json()
    print("Message received:", input, type(input))

    # Formulate a fake response.  Somehow connect this to an actual
    # Team object request; look at architecture
    global SD
    teamName = input["message"]
    try:
        team = SD.get_team(teamName)
    except:
        return jsonify({"/api/message": "team name failed to load"})
    response = {}
    response["team"] = str(teamName)
    response["year"] = str(team.get_year())
    response["coach"] = str(team.get_coach())
    # This returns a coach object, not a string.  Why tho
    response["numGames"] = str(team.num_games())
    response["numWins"] = str(team.num_wins())
    response["numLosses"] = str(team.num_losses())
    # return make_response(jsonify(response), 200)
    return jsonify(response)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

if __name__ == "__main__":
    app.run(debug=True)
