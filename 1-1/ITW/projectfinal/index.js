var vm = function () {
    console.log('ViewModel initiated...');
    //---Variáveis locais
    var self = this;
    self.searchUri = ko.observable('http://192.168.160.58/Formula1/api/Search/All');
    self.searchResults = ko.observableArray([])

    $("#search").autocomplete({
        minLength: 2,
        maxShowItems: 10,
        source: function (request, response) {
            $.ajax({
                url: self.searchUri() + '?q=' + $('#search').val(),
                success: function (data) {
                    self.searchResults(data)
                    response($.map(data, function (item) {
                        return item.Text + " | " + item.Source;
                    }));
                },
                error: function (data) {
                    console.log("error")
                }
            })
        },
        select: function (event, ui) {
            var array = ui.item.value.split(" | "), name = array[0], source = array[1]
            var id = ""
            console.log(self.searchResults())
            for (let i = 0; i < self.searchResults().length; i++) {
                if (self.searchResults()[i].Text === name) {
                    id = self.searchResults()[i].Id
                }
            }

            switch (source) {
                case "Driver":
                    window.location.href = "./driverDetails.html?id=" + id;
                    break
                case "Race":
                    window.location.href = "./raceDetails.html?id=" + id;
                    break
                case "Circuit":
                    window.location.href = "./circuitDetails.html?id=" + id;
                    break
                case "Constructor":
                    window.location.href = "./constructor.html?id=" + id;
                    break
                case "Country":
                    window.location.href = "./countryDetails.html?id=" + id;
                    break
            }
        }
    })



}
$(document).ready(function () {
    console.log("ready!");
    ko.applyBindings(new vm());
});



