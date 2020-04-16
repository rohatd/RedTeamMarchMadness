var year;

$("document").ready(function(){
    initSeasonData()

    // Send message for first team information.
    $("#send").click(function(){
        let message = $("#message").val();
        $.ajax({
            url: "http://localhost:5000/api/message/",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"message": message})
        }).done(function(data) {
            console.log(data);
            showText(data);
        });
    });
 
    // Send message for second team information.
    $("#send2").click(function(){
      let message2 = $("#message2").val();
      $.ajax({
        url: "http://localhost:5000/api/message/",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"message": message2})
      }).done(function(data) {
        console.log(data);
        showText2(data);
      });
    });

    // Send query for Stats page.
    $("#statQuery").click(function(){
      let statQuery = $("#statInput").val();
      $.ajax({
        url: "http://localhost:5000/api/get-stats/",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"query": statQuery})
      }).done(function(data) {
        console.log(data);
        showStats(data);
      });
    });

});

// Initialize the (most recent) SeasonData object, primarily for team comparison
function initSeasonData() {
  $.ajax({
      url: "http://localhost:5000/api/init/",
      type: "POST",
      data: JSON.stringify({"marchMadness.py, init_sd()": "Template Message"})
  }).done(function(data) {
      console.log(data);
      year = data.year
  });
}

// TODO: Simplify / generalize these showText functions.
// Displays the text within the corresponding object ID.
function showText(data) {
  document.getElementById("teamName").innerHTML = "Team: " + data.team;
  document.getElementById("year").innerHTML = "Year: " + data.year;
  document.getElementById("coach").innerHTML = "Coach: " + data.coach;
  document.getElementById("numGames").innerHTML = "Number of games: " + data.numGames;
  document.getElementById("numWins").innerHTML = "Number of wins: " + data.numWins;
  document.getElementById("numLosses").innerHTML = "Number of losses: " + data.numLosses;
}

function showText2(data) {
  document.getElementById("teamName2").innerHTML = "Team: " + data.team;
  document.getElementById("year2").innerHTML = "Year: " + data.year;
  document.getElementById("coach2").innerHTML = "Coach: " + data.coach;
  document.getElementById("numGames2").innerHTML = "Number of games: " + data.numGames;
  document.getElementById("numWins2").innerHTML = "Number of wins: " + data.numWins;
  document.getElementById("numLosses2").innerHTML = "Number of losses: " + data.numLosses;
}

// Set year to display for Team Comparison page.
function setYear(data) {
  document.getElementById("season-year").innerHTML += year;
}

// Show the stats on the Stats page
function showStats(data){
  let team_data = data["Team"];
  let coach_data = data["Coach"];
  // Construct the tables
  let teamtable = "";
  let coachtable = "";
  for (let key in team_data){
    let value = team_data[key];
    teamtable = teamtable + "<tr><th>" + key + "</th><td>" + value + "</td></tr>";
  }
  for (let key in coach_data){
    let value = coach_data[key];
    coachtable = coachtable + "<tr><th>" + key + "</th><td>" + value + "</td></tr>";
  }
  document.getElementById("statTeamTitle").innerHTML = "Team";
  document.getElementById("statCoachTitle").innerHTML = "Coach";
  document.getElementById("team-stat-table").innerHTML = teamtable;
  document.getElementById("coach-stat-table").innerHTML = coachtable;
}
