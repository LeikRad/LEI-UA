var previousSelection = "#Consumer"

$(document).ready(function () {
    $("#Comercial").hide()
    $("#Charity").hide()
})


$('#TipoUtilizador').change(function () {
    $(previousSelection).hide();
    previousSelection = '#' + this.value;
    $(previousSelection).show();
});

$('#Submit').click(function () {
    var ver = true;
    var typeofcustomer = $("#TipoUtilizador").val()
    if (typeofcustomer != "Consumer") {
        if ($.trim($("#Local" + typeofcustomer).val()).length < 10 || $.trim($("#Local" + typeofcustomer).val()).length > 100) {
            ver = false
            $("#LocalError" + typeofcustomer).addClass("d-block")
            $("#LocalError" + typeofcustomer).removeClass("d-none ")
        } else {
            $("#LocalError" + typeofcustomer).removeClass("d-block")
            $("#LocalError" + typeofcustomer).addClass("d-none ")
        }
        if ($.trim($("#Owner" + typeofcustomer).val()) == "") {
            ver = false
            $("#OwnerError" + typeofcustomer).addClass("d-block")
            $("#OwnerError" + typeofcustomer).removeClass("d-none ")
        } else {
            $("#OwnerError" + typeofcustomer).removeClass("d-block")
            $("#OwnerError" + typeofcustomer).addClass("d-none ")
        }
    }
    if (($.trim($("#Email" + typeofcustomer).val())).length < 10 || ($.trim($("#Email" + typeofcustomer).val())).length > 100 || ($("#Email" + typeofcustomer).val()).indexOf("@") == -1 || ($("#Email" + typeofcustomer).val()).lastIndexOf(".") < ($("#Email" + typeofcustomer).val()).indexOf("@")) {
        ver = false
        $("#EmailError" + typeofcustomer).addClass("d-block")
        $("#EmailError" + typeofcustomer).removeClass("d-none ")
    } else {
        $("#EmailError" + typeofcustomer).removeClass("d-block")
        $("#EmailError" + typeofcustomer).addClass("d-none ")
    }
    if (($.trim($("#Name" + typeofcustomer).val())).length < 10 || ($.trim($("#Name" + typeofcustomer).val())).length > 100) {
        ver = false
        $("#NomeError" + typeofcustomer).addClass("d-block")
        $("#NomeError" + typeofcustomer).removeClass("d-none")
    } else {
        $("#NomeError" + typeofcustomer).removeClass("d-block")
        $("#NomeError" + typeofcustomer).addClass("d-none")
    }
    if (($.trim($("#Password" + typeofcustomer).val())).length < 6) {
        ver = false
        $("#PasswordError" + typeofcustomer).addClass("d-block")
        $("#PasswordError" + typeofcustomer).removeClass("d-none")
    } else {
        $("#PasswordError" + typeofcustomer).removeClass("d-block")
        $("#PasswordError" + typeofcustomer).addClass("d-none")
    }
    if (($.trim($("#Password" + typeofcustomer).val())) != ($.trim($("#PasswordConf" + typeofcustomer).val()))) {
        ver = false
        $("#PasswordConfError" + typeofcustomer).addClass("d-block")
        $("#PasswordConfError" + typeofcustomer).removeClass("d-none")
    } else {
        $("#PasswordConfError" + typeofcustomer).removeClass("d-block")
        $("#PasswordConfError" + typeofcustomer).addClass("d-none")
    }
    if (!($('#Terms').is(":checked"))) {
        ver = false
        $("#TermsError").addClass("d-block")
        $("#TermsError").removeClass("d-none")
    } else {
        $("#TermsError").removeClass("d-block")
        $("#TermsError").addClass("d-none")
    }

    if (ver) {
        console.log(typeofcustomer)
        switch (typeofcustomer) {
            case 'Consumer':
                console.log(1)
                window.location.href = "https://wastenever.github.io/mainmenuConsumer.html";
                break;
            case 'Comercial':
                console.log(2)
                window.location.href = "https://wastenever.github.io/restaurantMain.html"
                break;
            case 'Charity':
                console.log(3)
                window.location.href = "https://wastenever.github.io/Charityoffers.html"
                break;

        }
    }
})

