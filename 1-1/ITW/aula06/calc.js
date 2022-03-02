var operacao = "+"
function getOperacao() {
    var e = document.getElementById("operacao")
    operacao = e.options[e.selectedIndex].value;
    console.log(operacao);
};

function getResult() {
    var op1 = document.getElementById("op1")
    var op2 = document.getElementById("op2")
    var res = document.getElementById("res")
    switch (operacao) {
        case "+":
            res.value = parseFloat(op1.value) + parseFloat(op2.value)
            break;
        case "-":
            res.value = parseFloat(op1.value) - parseFloat(op2.value)
            break;
        case "*":
            res.value = parseFloat(op1.value) * parseFloat(op2.value)
            break;
        case ":":
            if (op2.value == 0) {

                alert("Divisão impossivel")
                break
            }
            res.value = parseFloat(op1.value) / parseFloat(op2.value)
            break;
        case "%":
            if (op2.value == 0) {
                alert("Divisão impossivel")
                break
            }
            res.value = parseFloat(op1.value) % parseFloat(op2.value)
            break;
        case "!":
            if (op1.value = 1) {
                alert("op1 é menor que 1, fatorial só para numeros positivos")
                break
            }
            res.value = 1
            for (let i = 2; i <= op1.value; i++) {
                res.value = res.value * i
            }
            break;
        default:
            alert("erro, operaçao nao definida")
    }
}