var stocky = angular.module('stocky', []);

stocky.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

stocky.factory('$chart', function(){
    google.load('visualization', '1', {'packages':['annotationchart']});
    return new google.visualization.AnnotationChart(document.getElementById('chart_div'));
});

stocky.controller('StockDataController', ['$scope', '$http', '$chart', function($scope, $http, $chart){
    $scope.search = function(symbol) {
        $http.get('stock/' + symbol).then(function(result){
           ($scope.trend = _.first(result.data.trends)) && $scope.displayChart();
        });
    }

    $scope.displayChart = function(){
            var data = new google.visualization.DataTable();

            data.addColumn('date', 'Date');
            data.addColumn('number', 'Price');
            data.addColumn('string', 'Event');

            _.forEach($scope.trend.prices, function(item){
                var row = [new Date(item.date), item.price, item.event ? item.event: null];
                data.addRow(row);
            });

            $chart.draw(data, { displayAnnotations: true });
    }
}]);