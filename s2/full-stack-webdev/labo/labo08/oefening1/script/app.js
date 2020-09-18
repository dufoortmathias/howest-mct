'use strict';

function drawChart(labels, data) {
    let ctx = document.querySelector('.js-chart').getContext('2d');

    let config = {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: "iPhone",
                    backgroundColor: "white",
                    borderColor: "red",
                    data: data,
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: "Chart.js Line Chart"
            },
            tooltips: {
                mode: "index",
                intersect: true
            },
            hover: {
                mode: "nearest",
                intersect: true
            },
            scales: {
                xAxes: [
                    {
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: "Model"
                        }
                    }
                ],
                yAxes: [
                    {
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: "Prijs"
                        }
                    }
                ]
            }
        }
    };

    let myChart = new Chart(ctx, config);
}

//#region *** Callback-Visualisation - show____ ***
function showData(data) {
    console.log(data);

    let converted_labels = [];
    let converted_data = [];
    for (const iphone of data){
        converted_labels.push(iphone.unit);
        converted_data.push(iphone.price);
    }
    drawChart(converted_labels, converted_data);
}
//#endregion

//#region *** Data Access - get____ ***
function getIphoneData() {
    handleData('./iphone.json', showData);
}
//#endregion

//#region *** INIT / DOMContentLoaded ***
function init() {
    console.log('init geladen');
    getIphoneData();
}

document.addEventListener('DOMContentLoaded', () => {
    init();
})
//#endregion
