var MoistureChart = function () {
    this.init();
}

$.extend(MoistureChart.prototype, {
    init: function () {
        this.ctx = document.getElementById("moistureChart").getContext('2d');
        this.option = {
            responsive: true,
        };
        this.data = {
            datasets: [
                {
                    label: "My First dataset",
                    fillColor: "rgba(220,220,220,0.2)",
                    strokeColor: "rgba(220,220,220,1)",
                    pointColor: "rgba(220,220,220,1)",
                    pointStrokeColor: "#fff",
                    pointHighlightFill: "#fff",
                    pointHighlightStroke: "rgba(220,220,220,1)",
                },
                {
                    label: "My Second dataset",
                    fillColor: "rgba(151,187,205,0.2)",
                    strokeColor: "rgba(151,187,205,1)",
                    pointColor: "rgba(151,187,205,1)",
                    pointStrokeColor: "#fff",
                    pointHighlightFill: "#fff",
                    pointHighlightStroke: "rgba(151,187,205,1)",
                }
            ],
        }
    },

    setLabels: function (data) {
        this.data['labels'] = data;
    },

    setDatasetForMoisture: function (data) {
        this.data['datasets'][1]['data'] = data;
    },

    setDatasetForTemperature: function (data) {
        this.data['datasets'][0]['data'] = data;
    },

    drawChart: function () {
        var myLineChart = new Chart(this.ctx).Line(this.data, this.option); //'Line' defines type of the chart.
    }
});