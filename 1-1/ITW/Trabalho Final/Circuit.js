var vm = function () {
    console.log('ViewModel initiated...');
    //---Variáveis locais
    var self = this;
    self.baseUri = ko.observable('http://192.168.160.58/Formula1/api/Circuits');
    self.displayName = 'Circuits List';
    self.Circuits = ko.observableArray([]);
    self.error = ko.observable('');
    self.currentPage = ko.observable();
    self.pagesize = ko.observable(12);
    self.totalCircuits = ko.observable();
    self.hasPrevious = ko.observable(false);
    self.hasNext = ko.observable(false);
    self.updateIcons = function () {checkFavorites()}
    self.previousPage = ko.computed(function () {
        return self.currentPage() * 1 - 1;
    }, self);
    self.nextPage = ko.computed(function () {
        return self.currentPage() * 1 + 1;
    }, self);
    self.fromCircuits = ko.computed(function () {
        return self.previousPage() * self.pagesize() + 1;
    }, self);
    self.toCircuit = ko.computed(function () {
        return Math.min(self.currentPage() * self.pagesize(), self.totalCircuits());
    }, self);
    self.totalPages = ko.observable(0);
    self.pageArray = function () {
        var list = [];
        var size = Math.min(self.totalPages(), 9);
        var step;
        if (size < 9 || self.currentPage() === 1)
            step = 0;
        else if (self.currentPage() >= self.totalPages() - 4)
            step = self.totalPages() - 9;
        else
            step = Math.max(self.currentPage() - 5, 0);

        for (var i = 1; i <= size; i++)
            list.push(i + step);
        return list;
    };
    //--- Page Events
    self.activate = function (id) {
        console.log('CALL: getCircuits...');
        var composedUri = self.baseUri() + "?page=" + id + "&pagesize=" + self.pagesize();
        ajaxHelper(composedUri, 'GET').done(function (data) {
            console.log(data);
            hideLoading();
            self.Circuits(data.List);
            self.currentPage(data.CurrentPage);
            self.hasNext(data.HasNext);
            self.hasPrevious(data.HasPrevious);
            self.pagesize(data.PageSize)
            self.totalPages(data.PageCount);
            self.totalCircuits(data.Total);
            //self.SetFavourites();
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

    function getUrlParameter(sParam) {
        var sPageURL = window.location.search.substring(1),
            sURLVariables = sPageURL.split('&'),
            sParameterName,
            i;
        console.log("sPageURL=", sPageURL);
        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');

            if (sParameterName[0] === sParam) {
                return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
            }
        }

    };

    //--- start ....
    showLoading();
    var pg = getUrlParameter('page');
    console.log(pg);
    if (pg == undefined)
        self.activate(1);
    else {
        self.activate(pg);
    }


};

$(document).ready(function () {
    console.log("ready!");
    ko.applyBindings(new vm());
});
function checkFavorites() {
    $("i[id*='favourite_']").addClass("fa-heart-o")
    $("i[id*='favourite_']").removeClass("fa-heart")
    $("i[id*='favourite_']").parent().val("0")
    $.ajax({
        url: "http://192.168.160.58/Formula1/api/circuits",
        success: function (result) {
            var favoriteList = localStorage.getItem("circuitFavoriteList")
            if (favoriteList != null) {
                favoriteList = favoriteList.split(",")
                filtered = (result.List.filter(function (item) {
                    return favoriteList.includes(String(item.CircuitId))
                }));
                console.log(filtered)
                filtered.forEach(function (circuit) {
                    $("#favourite_" + circuit.CircuitId).addClass("fa-heart")
                    $("#favourite_" + circuit.CircuitId).removeClass("fa-heart-o")
                    $("#favourite_" + circuit.CircuitId).parent().val("1")
                })
            }

        }
    });
    $(".heart-button").click(function () {
        var id = $(this).find("i").attr("id")
        var value = $(this).val()
        var favorites = localStorage.getItem("circuitFavoriteList")
        if (favorites == null) {
            favorites = []
        }
        else {
            favorites = favorites.split(",")
        }
        id = id.split("_")[1]
        if (value == "0") {
            favorites.push(id)
            $(this).val("1")
        }
        else {
            $(this).val("0")
            favorites = favorites.filter(function (e) { return e != id })
        }
        $(this).find("i").toggleClass("fa-heart fa-heart-o")
        localStorage.setItem("circuitFavoriteList", favorites)
        console.log(localStorage.getItem("circuitFavoriteList"))
    })
    $(".card-img-top").hover(function () {
        $(this).animate({ margin: -10, width: "+=10", height: "+=10" });
        $(this).parent().animate({ margin: -5, width: "+=10", height: "+=10" });
    }, function () {
        $(this).animate({ margin: +10, width: "-=10", height: "-=10" });
        $(this).parent().animate({ margin: +10, width: "-=10", height: "-=10" });
    })
}
