$(document).ready(function () {
    $("#favoriteSelector").change(function () {
        var value = $("input[type='radio']:checked").val()
        switch (value) {
            case "drivers":
                $("iframe").attr("src", "favoriteDrivers.html");
                break
            case "constructors":
                $("iframe").attr("src", "favoriteConstructors.html");
                break
            case "countries":
                $("iframe").attr("src", "favoriteCountries.html");
                break
            case "nationalities":
                $("iframe").attr("src", "favoriteNationalities.html");
                break
            case "circuits":
                $("iframe").attr("src", "favoriteCircuits.html");
                break
        }
    })
})