var stocky = angular.module('stocky', ['angular-rickshaw']);

stocky.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

stocky.controller('StockDataController', ['$scope', '$http', function($scope, $http){

    $scope.search = function(symbol) {
        $http.get('stock/' + symbol).then(function(result){
            $scope.data = result.data;
        });
    }

}]);