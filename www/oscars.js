angular.module('oscars', [])
    .factory('DataFactory', function ($http) {
        return {
            getPopularityRank: function () {
                return $http.get('/data/pop.json');
            },
            getStateFrequency: function () {
                return $http.get('/data/states.json');
            },
            getBirdmanTime: function () {
                return $http.get('/data/time.json');
            }
        }
    })
    .directive('oscarsPopList', function () {
        return {
            templateUrl: '/templates/oscars-pop-list.tmplt.html',
            controller: function ($scope, DataFactory) {
                $scope.nominees = [];
                DataFactory.getPopularityRank().success(function (data) {
                    $scope.nominees = data;
                });
            }
        }
    })
    .directive('oscarsStatesPie', function () {
        return {
            templateUrl: '/templates/oscars-states-pie.tmplt.html'
        }
    })
    .directive('oscarsBirdmanTime', function () {
        return {
            templateUrl: '/templates/oscars-birdman-time.tmplt.html'
        }
    })
;