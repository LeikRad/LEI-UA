ko.bindingHandlers.safeSrc = {
    update: function (element, valueAccessor) {
        var options = valueAccessor()
        var srcImg = ko.unwrap(options.src)
        if (srcImg != null) {
            $(element).attr('src', srcImg);
        } else {
            $(element).attr('src', ko.unwrap(options.fallback));
        }
    }
};

var vm = function () {
    google.charts.load('current', { 'packages': ['corechart'] });

    console.log('ViewModel initiated...');
    //---Variáveis locais
    var self = this;
    self.searchUri = ko.observable('http://192.168.160.58/Formula1/api/Search/Drivers?q=');
    self.statsUri = ko.observable('http://192.168.160.58/Formula1/api/Statistics/Driver?id=')
    self.searchResults = ko.observableArray([])
    self.Career = ko.observableArray([])
    self.ImageUrl = ko.observable('')
    self.DriverName = ko.observable('')
    self.DriverId = ko.observable('')
    self.error = ko.observable('')
    self.Races = ko.observable('')
    self.Wins = ko.observable('')
    self.ShouldShow = ko.observable(false)


    $("#search").autocomplete({
        minLength: 2,
        maxShowItems: 10,
        source: function (request, response) {
            $.ajax({
                url: self.searchUri() + $('#search').val(),
                success: function (data) {
                    self.searchResults(data)
                    console.log(self.searchResults())
                    response($.map(data, function (item) {
                        return item.Name;
                    }));
                },
                error: function (data) {
                    console.log("error")
                }
            })
        },
        select: function (event, ui) {
            var Name = ui.item.value
            console.log(Name)
            console.log(self.searchResults())
            for (let i = 0; i < self.searchResults().length; i++) {
                if (self.searchResults()[i].Name === Name) {
                    id = self.searchResults()[i].DriverId
                }
            }
            showLoading()
            self.activate(id)

        }
    })

    self.activate = function (id) {
        console.log('CALL: getDrivers...');
        var composedUri = self.statsUri() + id;
        ajaxHelper(composedUri, 'GET').done(function (data) {
            console.log(data);
            hideLoading();
            self.ImageUrl(data.ImageUrl)
            
            self.Career(data.Career);
            self.DriverName(data.Name);
            self.DriverId(data.DriverId);
            self.Wins(data.Wins);
            self.Races(data.Races);
            self.ShouldShow(true)
            drawChart();

        });
    };
    //--- Internal functions
    function ajaxHelper(uri, method, data) {
        self.error(''); // Clear error message
        return $.ajax({
            type: method,
            url: uri,
            dataType: 'json',
            contentType: 'application/json',
            data: data ? JSON.stringify(data) : null,
            error: function (jqXHR, textStatus, errorThrown) {
                console.log("AJAX Call[" + uri + "] Fail...");
                hideLoading();
                self.error(errorThrown);
            }
        });
    }

    function sleep(milliseconds) {
        const start = Date.now();
        while (Date.now() - start < milliseconds);
    }



    function showLoading() {
        $("#myModal").modal('show', {
            backdrop: 'static',
            keyboard: false
        });
    }
    function hideLoading() {
        $('#myModal').on('shown.bs.modal', function (e) {
            $("#myModal").modal('hide');
        })
    }

    function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Year');
        data.addColumn('number', 'Points');
        data.addColumn('number', 'Position');
        for (let i = self.Career().length -1; i > -1; i--) {
            data.addRows([
                [(self.Career()[i].Year).toString(), self.Career()[i].Points, self.Career()[i].Position]
            ]);
        }
        var view = new google.visualization.DataView(data);
        view.setColumns([0, 1,
            // style column
            {
                calc: function (dt, row) {
                    if ((dt.getValue(row, 2) == 1)) {
                        return 'green';
                    } else {
                        return 'red';
                    }
                },
                type: 'string',
                role: 'style'
            },
            // annotation column
            {
                calc: 'stringify',
                sourceColumn: 2,
                type: 'string',
                role: 'annotation'
            }
        ]);



        // Set chart options
        var options = {
            title: "Career Overview:",
            bar: { groupWidth: "65%" },
            width: '100%',
            legend: {
                position: 'none'
            },
            chartArea: {
                // leave room for y-axis labels
                width: '100%',
            }
        };

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
        chart.draw(view, options);
    }
}
$(document).ready(function () {
    console.log("ready!");
    ko.applyBindings(new vm());
});



