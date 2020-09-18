"use strict";

let htmlPlaceholderSpellen;
let data;

function verwerkData(json) {
    data = json;
    //overloop de json en vul de innerHTML op met een <option> tag
    let html = "";
    for (let speldoos of data) {
        htmlPlaceholderSpellen.innerHTML += `<option value="${speldoos.gameId}">${speldoos.name}</option>`;
    }
}

function loadData() {
    fetch("https://www.diero.be/MCT/JSON/spellen.json")
        .then(function(response) {
            if (!response.ok) {
                console.log("response niet OK");
                throw Error(`Er is een probleem bij het fetchen: ${response.status}`);
            } else {
                return response.json();
            }
        })
        .then(json => verwerkData(json));
}

function toonAfbeelding() {
    let id = htmlPlaceholderSpellen.value;
    for (let speldoos of data) {
        if (speldoos.gameId == id) {
            document.querySelector(".js-spel").innerHTML = `<img src="${speldoos.thumbnail}" alt="" id="flag">`;
            break;
        }
    }
}

function setValidity(e) {
    let html = e.target;
    html.title = 
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("content loaded");
    htmlPlaceholderSpellen = document.querySelector(".js-spel-placeholder");
    htmlPlaceholderSpellen.addEventListener("input", toonAfbeelding);
    loadData();

    document.querySelector('.js-voornaam').addEventListener('invalid', setValidity);

});
