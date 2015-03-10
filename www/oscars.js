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
            template: '<div class="oscars-pie"></div>',
            replace: true,
            controller: function ($scope, DataFactory) {
                $scope.states = [];
                DataFactory.getStateFrequency().success(function (data) {
                    var temp = [];
                    for(var state in data) {
                        if(data.hasOwnProperty(state)) {
                            temp.push({
                                label: state,
                                data: data[state]
                            });
                        }
                    }
                    $scope.states = temp.slice(0);
                });
            },
            require: 'oscarsStatesPie',
            link: function (scope, el) {
                scope.$watch('states', function (n) {
                    if(n.length !== 0) {
                        createGraph(n);
                    }
                });

                function createGraph(data) {
                    $.plot(el[0], data, {
                        series: {
                            pie: {
                                show: true,
                                innerRadius: 0.5,
                                combine: {
                                    //threshold: 0.01
                                },
                                label: {
                                    threshold: 0.025
                                }
                            }
                        },
                        legend: {
                            show: false
                        },
                        grid: {
                            hoverable: true
                        },
                        tooltip: true,
                        tooltipOpts: {
                            content: function (label, xval, yval) {
                                return label + ' | ' + yval + ' tweets'
                            }
                        }
                    });
                }
            }
        }
    })
    .directive('oscarsBirdmanTime', function () {
        return {
            templateUrl: '/templates/oscars-birdman-time.tmplt.html',
            controller: function ($scope, DataFactory) {
                DataFactory.getBirdmanTime().success(function (data) {
                    $scope.time = data.time
                });
            }
        }
    })
;