function shuffle() {
    var red = document.getElementById("red")
    var blue = document.getElementById("blue")
    var green = document.getElementById("green")
    var yellow = document.getElementById("yellow")
    red.style.left = Math.floor(Math.random() * (window.innerWidth-100)) + "px"
    red.style.top = Math.floor(Math.random() * (window.innerHeight-100)) + "px"
    green.style.left = Math.floor(Math.random() * (window.innerWidth-100)) + "px"
    green.style.top = Math.floor(Math.random() * (window.innerHeight-100)) + "px"
    yellow.style.left = Math.floor(Math.random() * (window.innerWidth-100)) + "px"
    yellow.style.top = Math.floor(Math.random() * (window.innerHeight-100)) + "px"
    blue.style.left = Math.floor(Math.random() * (window.innerWidth-100)) + "px"
    blue.style.top = Math.floor(Math.random() * (window.innerHeight-100)) + "px"
}

function overDetails() {
    var x = event.target.id;
    var y = document.getElementById(x)
    var text = document.getElementById("text")
    text.innerText = "Olá eu sou o " + x + "\n Top:" + y.style.top + "\n Left:" + y.style.left
}


function clearInfo() {
    var text = document.getElementById("text")
    text.innerText = ""
}
window.onload = shuffle;