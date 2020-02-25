# Flask message handler
# Make sure you export the flask path: "$ export FLASK_APP=handler.py"
# Reference: https://medium.com/@gokhang1327/separate-front-end-from-back-end-with-flask-ajax-a5b22b12d001
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api/', methods=["POST"])
def main_interface():
    input = request.get_json()
    print("Message received:", input, type(input))

    # Formulate a fake response.  Somehow connect this to an actual
    # Team object request; look at architecture
    response = {}
    response["team"] = input["message"]
    response["W-L"] = 0.734
    response["numWins"] = 11
    response["numLosses"] = 2
    response["overall"] = "NCAA"
    return jsonify(response)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

if __name__ == "__main__":
    app.run(debug=True)
