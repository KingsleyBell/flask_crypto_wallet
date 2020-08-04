google.charts.load('current', {'packages': ['corechart']});
$(document).ready(function () {
  $("#wallet-nav").addClass('text-dark');
  google.charts.setOnLoadCallback(drawChart);
});

var btcChartData = [['Date', 'BTC Balance']],
  zarChartData = [['Date', 'ZAR Balance']];
for (let i = 0; i < btcData.length; i++) {
  btcChartData.push([
    new Date(btcData[i][0].trim()),
    btcData[i][1]
  ]);
}
for (i = 0; i < zarData.length; i++) {
  zarChartData.push([
    new Date(zarData[i][0].trim()),
    zarData[i][1]
  ]);
}

function drawChart() {
  let btcData = google.visualization.arrayToDataTable(btcChartData),
    zarData = google.visualization.arrayToDataTable(zarChartData),
    dataJoin = google.visualization.data.join(btcData, zarData, 'full', [[0, 0]], [1], [1]);;

  let options = {
    title: 'BTC and ZAR balances over time',
    width: '100%',
    height: 500,
    chartArea : { left: '7%' },
    legend: {position: 'bottom'},
    // Gives each series an axis that matches the vAxes number below.
    series: {
      0: {targetAxisIndex: 0},
      1: {targetAxisIndex: 1}
    },
    vAxes: {
      // Adds titles to each axis.
      0: {title: 'BTC'},
      1: {title: 'ZAR'}
    },
    colors: ['#613dc1', '#858ae3'],
    explorer: {
      a: 'horizontal',
      keepInBounds: true,
      maxZoomIn: 12.0,
      zoomDelta: 1.1
    }
  };

  var btcChart = new google.visualization.LineChart(document.getElementById('btc_chart'));
  btcChart.draw(dataJoin, options);
}