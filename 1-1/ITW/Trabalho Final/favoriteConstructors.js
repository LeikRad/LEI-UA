// ViewModel KnockOut
var filtered = []
var vm = function () {
    console.log('ViewModel initiated...');
    //---Variáveis locais
    var self = this;
    self.baseUri = ko.observable('http://192.168.160.58/Formula1/api/constructors');
    //self.baseUri = ko.observable('http://localhost:62595/api/constructors');
    self.updateList = function () {
        checkFavorites()
    }
    self.displayName = 'Favorite Constructors';
    self.error = ko.observable('');
    self.passingMessage = ko.observable('');
    self.records = ko.observableArray([]);
    self.currentPage = ko.observable(1);
    self.pagesize = ko.observable(20);
    self.totalRecords = ko.observable(50);
    self.hasPrevious = ko.observable(false);
    self.hasNext = ko.observable(false);
    self.previousPage = ko.computed(function () {
        return self.currentPage() * 1 - 1;
    }, self);
    self.nextPage = ko.computed(function () {
        return self.currentPage() * 1 + 1;
    }, self);
    self.fromRecord = ko.observable()
    self.toRecord = ko.observable()
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
        console.log('CALL: getConstructors...');
        var composedUri = self.baseUri() + "?page=" + id + "&pageSize=" + self.pagesize();
        ajaxHelper(composedUri, 'GET').done(function (data) {
            console.log(data);
            hideLoading();
            self.records(filtered);
            self.currentPage(data.CurrentPage);
            self.hasNext(data.HasNext);
            self.hasPrevious(data.HasPrevious);
            self.pagesize(data.PageSize)
            self.totalPages(data.PageCount);
            self.totalRecords(filtered.length);
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
    checkFavorites();
    viewmodel = new vm()
    ko.applyBindings(viewmodel);
});
function checkFavorites() {
    $.ajax({
        url: "http://192.168.160.58/Formula1/api/constructors",
        success: function (result) {
            var favoriteList = localStorage.getItem("constructorFavoriteList")
            console.log(localStorage.getItem("constructorFavoriteList"))
            if (favoriteList != null) {
                favoriteList = favoriteList.split(",")
                console.log(favoriteList)
                filtered = (result.List.filter(function (item) {
                    return favoriteList.includes(String(item.ConstructorId))
                }));
            }
            console.log(filtered)
            update_pagination()


        }
    });
    $(".details").click(function () {
        var value = $(this).val()
        window.parent.location.href = './constructorDetails.html?id=' + value
    })
}
$("table").on("click", ".heart-button", function () {
    var id = $(this).find("i").attr("id")
    id = id.split("_")[1]
    console.log(id)
    var favorites = localStorage.getItem("constructorFavoriteList")
    favorites = favorites.split(",")
    favorites = favorites.filter(function (e) { return e != id })
    localStorage.setItem("constructorFavoriteList", favorites)
    $(this).parent().parent().remove()
    update_pagination()
    viewmodel.totalRecords(parseInt(viewmodel.totalRecords()) - 1)
})


function update_pagination() {
    jQuery(function ($) {
        // consider adding an id to your table,
        // just incase a second table ever enters the picture..?
        var items = $("table tbody tr");

        var numItems = items.length;
        var perPage = 10;
        viewmodel.pagesize(perPage)
        var pagination_placeholder_selector = ".pagination-page"; // put in a variable to ensure proper changes in the future
        var myPageName = "#page-"; // a number will follow for each page

        // only show the first 2 (or "first per_page") items initially
        items.slice(perPage).hide();
        // now setup your pagination
        // you need that .pagination-page div before/after your table
        $(pagination_placeholder_selector).pagination({
            items: numItems,
            itemsOnPage: perPage,
            cssStyle: "compact-theme",
            hrefTextPrefix: myPageName,
            onPageClick: function (pageNumber) { // this is where the magic happens
                // someone changed page, lets hide/show trs appropriately
                var showFrom = perPage * (pageNumber - 1);
                if (numItems > perPage) {
                    var showTo = showFrom + perPage;
                }
                else {
                    var showTo = showFrom + numItems
                }
                if (showTo > numItems) {
                    showTo = numItems
                }
                viewmodel.fromRecord(showFrom+1)
                viewmodel.toRecord(showTo)
                items.hide() // first hide everything, then show for the new page
                    .slice(showFrom, showTo).show();
            }
        });


        // EDIT: extra stuff to cover url fragments (i.e. #page-3)
        // https://github.com/bilalakil/bin/tree/master/simplepagination/page-fragment
        // is more thoroughly commented (to explain the regular expression)

        // we'll create a function to check the url fragment and change page
        // we're storing this function in a variable so we can reuse it
        var checkFragment = function () {
            // if there's no hash, make sure we go to page 1
            var hash = window.location.hash || (myPageName + "1");

            // we'll use regex to check the hash string
            var re = new RegExp("^" + myPageName + "(\\d+)$");
            hash = hash.match(re);

            if (hash)
                // the selectPage function is described in the documentation
                // we've captured the page number in a regex group: (\d+)
                $(pagination_placeholder_selector).pagination("selectPage", parseInt(hash[1]));
        };

        // we'll call this function whenever the back/forward is pressed
        $(window).bind("popstate", checkFragment);

        // and we'll also call it to check right now!
        checkFragment();

        viewmodel.totalPages(Math.ceil(filtered.length/perPage))


    });
}