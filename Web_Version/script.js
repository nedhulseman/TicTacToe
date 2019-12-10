var board;
var players = {'player-1':"", 'player-2':""}
var turn = "player-1";
var winner = "";






function initiateGame(){
    board = ["", "", "", "", "", "", "", "", ""];
    players['player-1'] = document.getElementById("player-1-letter-text").innerHTML;
    players['player-2'] = document.getElementById("player-2-letter-text").innerHTML;
    turn = "player-1";
    winner = "";
    

    
}

function clearBoard() {
     board = ["", " ", "", "", "", "", "", "", ""];
   
}

function updateBoard(panel){

    
    if (document.getElementById("but-"+panel).innerHTML == ""  && winner == ""){
        document.getElementById("but-"+panel).innerHTML = players[turn];
        board[panel - 1] = players[turn];
        
        checkWinner()
        if (turn == "player-1" && winner == ""){
            turn = "player-2";
        } 
        else if (winner == ""){
            turn = "player-1";
        }
    }
    
}

function checkWinner(){
    if (board[0] == board[1] && board[1] == board[2] && board[0] != ""){
        winner = turn;
    }
    else if (board[0] == board[3] && board[3] == board[6] && board[0] != ""){
        winner = turn;
    }
    else if (board[0] == board[4] && board[4] == board[8] && board[0] != ""){
        winner = turn;
    }
    else if (board[1] == board[4] && board[4] == board[7] && board[1] != ""){
        winner = turn;
    }
    else if (board[2] == board[5] && board[5] == board[8] && board[2] != ""){
        winner = turn;
    }
    else if (board[2] == board[4] && board[4] == board[6] && board[2] != ""){
        winner = turn;
    }
    else if (board[3] == board[4] && board[4] == board[5] && board[3] != ""){
        winner = turn;
    }
    else if (board[6] == board[7] && board[7] == board[8] && board[6] != ""){
        winner = turn;
    }
    
    if (winner != ""){
        console.log("The winner is " + winner);
        document.getElementById("winner-text").innerHTML = "Player " + winner[winner.length - 1] + " Wins!";
        
    }
}


document.getElementById("switch-players").addEventListener("click", function(){
   if (document.getElementById("player-1-letter-text").innerHTML == "X" ){
       document.getElementById("player-1-letter-text").innerHTML = "O";
       document.getElementById("player-2-letter-text").innerHTML = "X" ;
   }
   else {
       document.getElementById("player-1-letter-text").innerHTML = "X";
       document.getElementById("player-2-letter-text").innerHTML = "O";
   }
});


document.getElementById("start-button").addEventListener("click", function(){
      if (document.getElementById("start-button").innerHTML == "Start Game" ){
        document.getElementById("start-button").innerHTML = "New Game";
        initiateGame()
      }
      
      else{
         document.getElementById("start-button").innerHTML = "Start Game";
         document.getElementById("winner-text").innerHTML = ""
         for (var panel=1; panel<10; panel++){
             document.getElementById("but-" + panel).innerHTML = ""
             players['player-1'] = "";
             players['player-2'] = "";

         }
      }
});




document.getElementById("but-1").addEventListener("click", function(){
    var panel = 1;
    updateBoard(panel);
});
document.getElementById("but-2").addEventListener("click", function(){
    var panel = 2;
    updateBoard(panel);

});
document.getElementById("but-3").addEventListener("click", function(){
    var panel = 3;
    updateBoard(panel);

});
document.getElementById("but-4").addEventListener("click", function(){
    var panel = 4;
    updateBoard(panel);

});
document.getElementById("but-5").addEventListener("click", function(){
    var panel = 5;
    updateBoard(panel);

});
document.getElementById("but-6").addEventListener("click", function(){
    var panel = 6;
    updateBoard(panel);

});
document.getElementById("but-7").addEventListener("click", function(){
    var panel = 7;
    updateBoard(panel);

});
document.getElementById("but-8").addEventListener("click", function(){
    var panel = 8;
    updateBoard(panel);

});
document.getElementById("but-9").addEventListener("click", function(){
    var panel = 9;
    updateBoard(panel);

});











