

$("document").ready(function(){
    initSeasonData()
    $("#send").click(function(){
        var message = $("#message").val();
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
});

function initSeasonData() {
  $.ajax({
      url: "http://localhost:5000/api/init/",
      type: "POST",
      data: JSON.stringify({"handler.py, init_sd()": message})
  }).done(function(data) {
      console.log(data);
  });
}

function showText(data) {
  // TODO: Parse data JSON
  document.getElementById("teamName").innerHTML = "Team: " + data.team;
  document.getElementById("year").innerHTML = "Year: " + data.year;
  document.getElementById("numGames").innerHTML = "Number of games: " + data.numGames;
  document.getElementById("numWins").innerHTML = "Number of wins: " + data.numWins;
  document.getElementById("numLosses").innerHTML = "Number of losses: " + data.numLosses;
}
