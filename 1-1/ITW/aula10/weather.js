$(document).ready(function () {
    function MyViewModel() {
        var self = this
        console.log(this)
        console.log(self)
        self.currentWeather = ko.observable();
        self.changedCity = function () {
            $.ajax({
                url: "http://api.openweathermap.org/data/2.5/weather",
                data: {
                    q: $("#citySelector").val(),
                    APPID: 'b2b1df463182c3cca5276e9d3267cc95'
                },
                success: function (data) {
                    if (data.name) {
                        self.currentWeather(data)
                        console.log(self.currentWeather())
                    }
                    else {
                        alert(data.message);
                    }
                },
                error: function () {
                    alert('Erro!');
                }
            });
        };
    }
    ko.applyBindings(new MyViewModel());
});