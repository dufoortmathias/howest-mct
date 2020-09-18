"use strict";

function checkValue() {
    const htmlGewicht = document.querySelector(".js-gewicht");
    const htmlLengte = document.querySelector(".js-lengte");
    const htmlKnop = document.querySelector(".js-knop");

    if ((htmlLengte.value >= 35 && htmlLengte.value <= 200) && (htmlGewicht.value >= 35 && htmlGewicht.value <= 200)) {
        htmlKnop.disabled = false;
    } else {
        htmlKnop.disabled = true;
    }
}

function init() {
    document.querySelector(".js-lengte").addEventListener("input", checkValue);
    document.querySelector(".js-gewicht").addEventListener("input", checkValue);
    document.querySelector(".js-knop").addEventListener("click", verzendNaarAPI);
}



function verzendNaarAPI() {
    console.log("asdf");
}



document.addEventListener("DOMContentLoaded", () => {
    console.log("Content loaded");
    checkValue();
    init();
    
});
