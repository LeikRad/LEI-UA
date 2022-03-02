
$('#TipoUtilizador').change(function () {
    console.log(this.value == "Consumer")
    if (this.value == "Consumer") {
        $("#PriceOn").addClass("d-block")
        $("#PriceOn").removeClass("d-none")
        $("#PriceOff").addClass("d-block")
        $("#PriceOff").removeClass("d-none")
    } else {
        $("#PriceOn").addClass("d-none")
        $("#PriceOn").removeClass("d-block")
        $("#PriceOff").addClass("d-none")
        $("#PriceOff").removeClass("d-block")
    }
});

$('#Submit').click(function () {
    var ver = true;
    if (($.trim($("#Produto").val())) == "") {
        ver = false
        $("#ProdutoError").addClass("d-block")
        $("#ProdutoError").removeClass("d-none ")
    } else {
        $("#ProdutoError").removeClass("d-block")
        $("#ProdutoError").addClass("d-none ")
    }
    if ($('#TipoUtilizador').val() == "Consumer") {
    if (($.trim($("#Price").val())) == "") {
        ver = false
        $("#PriceError").addClass("d-block")
        $("#PriceError").removeClass("d-none ")
    } else {
        $("#PriceError").removeClass("d-block")
        $("#PriceError").addClass("d-none ")
        }
    }
    if (($.trim($("#Time").val())).split(":").length != 3) {
        ver = false
        $("#TimeError").addClass("d-block")
        $("#TimeError").removeClass("d-none ")
    } else {
        $("#TimeError").removeClass("d-block")
        $("#TimeError").addClass("d-none ")
    }
    if (($("#imagefile").val()) == "") {
        ver = false
        $("#ImageError").addClass("d-block")
        $("#ImageError").removeClass("d-none ")
    } else {
        $("#ImageError").removeClass("d-block")
        $("#ImageError").addClass("d-none ")
    }
    if (ver) {
        window.location.href = "https://wastenever.github.io/restaurantMain.html";
    }
})