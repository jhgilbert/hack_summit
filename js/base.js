var kivaApp = angular.module('kivaApp', ['ngRoute']);

function mainCtrl($scope) {
    $scope.test = "Angular is working!";
}

kivaApp.config(['$routeProvider',
    function ($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: '../templates/home.html'
        }).
        when('/browse', {
            templateUrl: '../templates/browse.html'
        }).
        otherwise({
            redirectTo: '/'
        });
    }
]);

