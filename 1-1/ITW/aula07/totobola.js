var Results1 = 0;
var _Status1 = document.getElementById("Status1")
var ResultsX = 0;
var _StatusX = document.getElementById("StatusX")
var Results2 = 0;
var _Status2 = document.getElementById("Status2")

var gamedict = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0}

var game2 = 0;
var last_radioChanged = ""
var multiples = document.getElementsByName("multiplas");


/*
for (let i = 0; i < multiples.length; i++) {
    console.log(multiples[i].value)
}
*/

function boxClicked() {
    var array = event.target.id.replace("Jogo", "").split("_");
    var game = array[0];
    var result = array[1];
    var multiple_value = 1

    if (event.target.checked) {
        if (result == "1") {
            Results1++
        } else if (result == "2") {
            Results2++
        } else {
            ResultsX++
        }
        gamedict[game]++
    } else {
        if (result == "1") {
            Results1--
        } else if (result == "2") {
            Results2--
        } else {
            ResultsX--
        }
        gamedict[game]--
    }
    for (let i = 1; i <= Object.keys(gamedict).length; i++) {
        if (gamedict[i.toString()] == 0){
            continue
        } else {
            
            multiple_value = multiple_value * gamedict[i]
        }
    }
    
    for (let i = 0; i < multiples.length; i++) {
        if (multiple_value > 384) {
            document.getElementById(multiples[i].id).checked = false;
        } else if (multiple_value == multiples[i].value) {
            document.getElementById(multiples[i].id).checked = true;
            last_radioChanged = multiples[i].id
        } else {
            document.getElementById(multiples[i].id).checked = false;
        }
    }   
    _Status1.innerText = Results1;
    _Status2.innerText = Results2;
    _StatusX.innerText = ResultsX;
    
}