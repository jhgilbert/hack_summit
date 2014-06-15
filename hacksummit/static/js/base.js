var kivaApp = angular.module('kivaApp', ['ngRoute']);

function mainCtrl($scope) {
    $scope.test = "Angular is working!";
}

kivaApp.config(['$routeProvider',
    function ($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: '/static/templates/home.html'
        }).
        when('/browse', {
            templateUrl: '/static/templates/browse.html'
        }).
        otherwise({
            redirectTo: '/'
        });
    }
]);

