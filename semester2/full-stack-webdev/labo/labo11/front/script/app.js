"use strict";

const backend_IP = "http://localhost:5000";
const backend = backend_IP + "/api/v1";

//#region ***  DOM references ***
let html_mendeljev;
let html_info;
let html_filter;
//#endregion

//#region ***  Callback-Visualisation - show___ ***
function showFilters(json) {
    html_filter.innerHTML = "";
    for (let data of json) {
        let str = `<div data-typeid="${data.typeID}" class="js-filter-type c-filter--type c-filter--type-${data.typeCode}">${data.type}</div>`;
        html_filter.innerHTML += str;
    }
}

function showElements(json) {
    html_mendeljev.innerHTML = "";
    for (let data of json) {
        let str = `<div data-atomic="${data.atomicNumber}" class="js-element c-mendelelement o-gridrow-${data.displayRow} o-gridcol-${data.displayColumn} c-mendelelement--${data.typeCode}">
                    <div class="c-mendelelement__atomicnumber">${data.atomicNumber}</div>
                    <div class="c-mendelelement__symbol">${data.symbol}</div>
                </div>`;
        html_mendeljev.innerHTML += str;
    }
    listenToElement();
}

function showInfo(info) {
    html_info.innerHTML = `Symbol: ${info.symbol} - ${info.name} - ${info.discoverer}`;
    console.log(info);
}
//#endregion

//#region ***  Callback-No Visualisation - callback___  ***
//#endregion

//#region ***  Data Access - get___ ***
function getTypes() {
    handleData(backend + "/types", showFilters);
}

function getElements() {
    handleData(backend + "/elementen", showElements);
}

function getElementsByID(id) {
    console.log(id);
    handleData(backend + "/elementen/types/" + id, showElements);
}

function getInfo(id) {
    handleData(backend + "/elementen/" + id, showInfo);
}
//#endregion

//#region ***  Event Listeners - listenTo___ ***
function listenToFilter() {
    let btns = document.querySelectorAll(".js-filter");
    for (let btn of btns) {
        btn.addEventListener("click", (e) => {
            getElementsByID(e.target.dataset.typeid);
        });
    }
}
function listenToElement() {
    let elements = document.querySelectorAll(".js-element");
    console.log(elements.length);
    for (let element of elements) {
        element.addEventListener("mouseover", (e) => {
            getInfo(element.dataset.atomic);
        });
    }
}
//#endregion

//#region ***  INIT / DOMContentLoaded  ***
const init = function () {
    html_filter = document.querySelector(".js-filter");
    html_mendeljev = document.querySelector(".js-mendeljev");
    html_info = document.querySelector(".js-info");
    getTypes();
    getElements();
    listenToFilter();
};
//#endregion

document.addEventListener("DOMContentLoaded", init);
