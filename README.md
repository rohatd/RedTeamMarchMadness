# RedTeamMarchMadness
RPISDDSpring2020


# Requirments and Installation Instructions
The March Madness Predictor application can be run locally as a web application. First, Python3 needs to be installed. Directions to install python can be found here: https://www.python.org/downloads/. 

Next, flask needs to be installed with a virtual environment. Instructions on how to install flask with a virtual environment can be found here: https://flask.palletsprojects.com/en/1.1.x/installation/. 

To run the application,  the server needs to be started. First, activate the virtual environment and navigate to the directory where the source code is located using the cd command. Make sure the following requirements are installed before beginning the server: sklearn, sportsreference, and pandas. Documentation of these packages can be found here respectively: https://pypi.org/project/sklearn/ ,https://pypi.org/project/sportsreference/, https://pypi.org/project/pandas/  .

 To install these packages, use the following commands: 


  $ pip install sklearn 

  $ pip install sportsreference

  $ pip install pandas 


To start the server on Unix, Linux or macOS, use the following commands


  $ export FLASK_APP=marchMadness.py

  $ FLASK_DEBUG=1

  $ python marchMadness.py


If using Windows, use ‘set’ instead of ‘export’.


The server is now started. To launch the application, type the url of the localhost into the internet browser (Chrome, Firefox or Safari recommended). The address will be found in the bash shell after starting the server. (Line will read something like “Running on http://127.0.0.1.5000/”). If styling does not appear, press Ctrl +Shift +  r. This will refresh the page and clear the cache. 


You can now navigate around the application, compare and view team statistics, and view the predicted 2019 March Madness bracket.

