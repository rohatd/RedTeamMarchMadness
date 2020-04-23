from flask import Flask, render_template, url_for, request, jsonify
from seasondata import *
from bracket import *
from collections import deque
import json

app = Flask(__name__)
SD =None
B = None 


# Request Handling
@app.route('/api/init/', methods=["GET", "POST"])
def init_sd():
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
	return render_template('homepage.html')

@app.route("/team-compare")
def teamCompare():
	return render_template('teamCompare.html')

@app.route("/generate-bracket")
def generateBracket():

	teamList = deque()
	teams = []
	file = open("bracket.txt", 'r')
	for l in file:
		teams.append(l.strip())
		
	# global B
	# try:
	# 	B = Bracket(teamList)
	# except: 
	# 	print("bracket: something went wrong.")


	# teams = B.getBracket()
	#print(teams)
	return render_template('generateBracket.html', teams= teams)

@app.route("/stats")
def stats():
	return render_template('stats.html')


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
	input = request.get_json()
	print("Message received:", input, type(input))

	global SD
	t1 = input["message1"]
	t2 = input["message2"]
	teamName1 = t1[6:]
	teamName2 = t2[6:]

	try:
		team1 = SD.get_team(teamName1)
		team2 = SD.get_team(teamName2)

	except:
		return jsonify({"/api/compare": "team name failed to load"})
	response1 = {}

	print("OKAY")
	response1["numWins"] = str(team1.num_wins())
	response1["homeWins"] = str(team1.get_attribute("W.2_x"))
	response1["awayWins"] = str(team1.get_attribute("W.3_x"))
	response1["rating"] = str(team1.get_attribute("SRS_x"))
	response1["w_l_p"] = str(team1.get_attribute("W-L%_x"))

	response1["numWins2"] = str(team2.num_wins())
	response1["homeWins2"] = str(team2.get_attribute("W.2_x"))
	response1["awayWins2"] = str(team2.get_attribute("W.3_x"))
	response1["rating2"] = str(team2.get_attribute("SRS_x"))
	response1["w_l_p2"] = str(team2.get_attribute("W-L%_x"))


	response = {}
	if int(response1["homeWins2"]) > int(response1["homeWins"]):
		response["homeWins"] = teamName2
	else:
		response["homeWins"] = teamName1 

	if int(response1["awayWins2"]) > int(response1["awayWins"]):
		response["awayWins"] = teamName2
	else:
		response["awayWins"] = teamName1 

	if float(response1["rating2"]) > float(response1["rating"]):
		response["rating"] = teamName2
	else:
		response["rating"] = teamName1 

	if float(response1["w_l_p2"]) > float(response1["w_l_p"]):
		response["w_l_p"] = teamName2
	else:
		response["w_l_p"] = teamName1 


	print(response)
	return jsonify(response)



@app.route('/api/get-stats/', methods=["POST"])
def getStats():
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
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	return response

@app.route('/api/get-teams', methods=["POST"])
def getTeams():
	try:
		teams = SD.getTeams()
	except:
		return jsonify({"/api/get-teams": "Fail"})


if __name__ == "__main__":
	app.run(debug=True)
