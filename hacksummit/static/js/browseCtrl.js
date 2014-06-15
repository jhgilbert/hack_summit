function browseCtrl($scope, $http) {

    // Angular's ng-repeat does not get along with Carousel -- this hack is ugly but time is short :)
    function makeCarouselElement(loan) {
        if (loan.fb_friend) {
            return "<div class=\"carousel-element\" style=\"padding-top: 10px; background-image: url('http:\/\/www.kiva.org\/img\/w290\/" + loan.image.id + ".jpg');\"><div class=\"sm-preview\"><h3 class=\"sm-preview-head\">" + loan.name + "</h3><p class='sm-preview-country'>" + loan.location.country + "</p></p><p class='sm-preview-text'>Loan " + loan.use.replace("To","to") + "</p></div><div class='friend-funding'><div class='friend-funding-icon'><img src='/static/img/fb.png' style='height: 18px; width: auto; margin-right: 3px;'></div><div class='friend-funding-text'>" + loan.fb_friend + " funded this</div></div></div>";
        }
        return "<div class=\"carousel-element\" style=\"padding-top: 10px; background-image: url('http:\/\/www.kiva.org\/img\/w290\/" + loan.image.id + ".jpg');\"><div class=\"sm-preview\"><h3 class=\"sm-preview-head\">" + loan.name + "</h3><p class='sm-preview-country'>" + loan.location.country + "</p></p><p class='sm-preview-text'>Loan " + loan.use.replace("To","to") + "</p></div></div>";
    }

    $http.get('/api/lender/picks').success(function(data) {
        $scope.loans = data.results;

        angular.forEach($scope.loans, function(loan, idx) {
            if (idx == 1) {
                loan.fb_friend = "Jennifer Gilbert";
            } else if (idx == 3) {
                loan.fb_friend = "Jose Marietta";
            } else {
                if (idx % 3 == 0 && idx !== 0) {
                    loan.fb_friend = "Rachel Sanders";
                }
            }
        });

        var carouselHtmlString = "";

        angular.forEach($scope.loans, function (loan, idx) {
            carouselHtmlString += makeCarouselElement(loan);
        });

        $('#recommendations').append(carouselHtmlString);

        $("#recommendations").owlCarousel({
            pagination: true,
            autoPlay: 4000,
            // navigation: true,
            items: 2,
            itemsScaleUp: false
            // rewindSpeed: 0
        });
    });

}