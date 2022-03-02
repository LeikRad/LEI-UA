var start = true;
var control = 1;
var op1 = "";
var op2 = "";
var operation = "";
var res = document.getElementById("res");

function addNumber() {
    var x = event.target.value;
    if (control == 1) {
        op1 = op1 + x;
    } else {
        op2 = op2 + x;
    } if (start) {
        res.innerText = "";
        start = false;
    }
    res.innerText += x;
}




function addOperation() {
    if (start) {
        start = false
        res.innerText = "0"
        op1 = "0"
    }
    operation = event.target.value;
    if (control == 1) {
        control = 2;
        res.innerText += operation;
    } else {
        res.innerText = "Erro!!";
    }
}

function calculate() {
    control = 1
    switch (operation) {
        case "+":
            op1 = parseFloat(op1) + parseFloat(op2);
            op2 = ""
            res.innerText = op1;
            break;
        case "-":
            op1 = parseFloat(op1) - parseFloat(op2);
            op2 = ""
            res.innerText = op1;
            break;
        case "*":
            op1 = parseFloat(op1) * parseFloat(op2);
            op2 = ""
            res.innerText = op1
            break;
        case "/":
            if (op2 == 0) {
                res.innerText = "Erro!!";
                start = true
                break;
            } else {
                op1 = parseFloat(op1) / parseFloat(op2);
                op2 = ""
                res.innerText = op1
            }
            break;

    }
}

function clearResult() {
    start = true;
    control = 1;
    op1 = "";
    op2 = "";
    operation = "";
    res.innerText="0"
}