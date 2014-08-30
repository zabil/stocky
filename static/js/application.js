var stocky = angular.module('stocky', []);

stocky.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

stocky.controller('StockDataController', ['$scope', '$http', function($scope, $http){

    $scope.search = function(symbol) {
        $http.get('stock/' + symbol).then(function(result){
            $scope.trend = _.first(result.data.trends);
            if($scope.trend){
                $scope.data = {
                  labels:[],
                  series: [
                        _.flatten(_.first(result.data.trends).prices, 'price')
                  ]
                }
             }
             Chartist.Line('.stock-chart', $scope.data);
        });
    }

}]);