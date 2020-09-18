"use strict";

function init() {
    //koppel een event aan het veranderen van de range van de score
    document.querySelector(".js-range").addEventListener("input", toonPunten);
}

function toonPunten(){
    let score = document.querySelector(".js-range").value;
    console.log(score);
    document.querySelector(".js-placeholder-score").innerHTML = `${score}/10`;
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM geladen");
    init();
});