var CurrentAccounts = {
    "ConsumerEmailtest@gmail.com": [{ "Password": "ConsumerPassword", "TypeOfAccount": "Consumer", "Nome": "ConsumerName" }],
    "ComercialEmailtest@gmail.com": [{ "Password": "ComercialPassword", "TypeOfAccount": "Comercial", "Nome": "ComercialName", "Dono": "NomedoDono", "Local": "Rua do Comerciante" }],
    "CharityEmailtest@gmail.com": [{ "Password": "CharityPassword", "TypeOfAccount": "Charity", "Nome": "CharityName", "Dono": "NomedoDono", "Local": "Rua da Charity" }]
}

$('#Submit').click(function () {
    ver = true
    if (($.trim($("#Email").val())) == "") {
        ver = false
        $("#EmailError").addClass("d-block")
        $("#EmailError").removeClass("d-none ")
    } else {
        $("#EmailError").removeClass("d-block")
        $("#EmailError").addClass("d-none ")
    }
    if (($.trim($("#Password").val())) == "") {
        ver = false
        $("#PasswordError").addClass("d-block")
        $("#PasswordError").removeClass("d-none ")
    } else {
        $("#PasswordError").removeClass("d-block")
        $("#PasswordError").addClass("d-none ")
    }

    if (ver) {
        if (CurrentAccounts.hasOwnProperty(($.trim($("#Email").val())))) {
            if (CurrentAccounts[($.trim($("#Email").val()))][0].Password == ($.trim($("#Password").val()))) {
                switch (CurrentAccounts[($.trim($("#Email").val()))][0].TypeOfAccount) {
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
            } else {
                $("#AccountdetailsError").addClass("d-block")
                $("#AccountdetailsError").removeClass("d-none ")
            }
        } else {
            $("#AccountdetailsError").addClass("d-block")
            $("#AccountdetailsError").removeClass("d-none ")

        }
    }

});