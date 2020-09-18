"use strict";

//#region ***  DOM references ***
let html_kleurenHolder, html_uitvoerHolder;
//#endregion

//#region ***  Callback-Visualisation - show___ ***
function showKleuren(jsonObject) {
    let kleurenHtml = "";
    for (const kleur of jsonObject.colors) {
        kleurenHtml += `<li class="js-kleurelement" data-code="${kleur.code.hex}" data-category="${kleur.category}">${kleur.color}</li>`;
    }
    html_kleurenHolder.innerHTML = kleurenHtml;
    listenToClickKleur();
}
//#endregion

//#region ***  Callback-No Visualisation - callback___  ***
//#endregion

//#region ***  Data Access - get___ ***
function getKleuren() {
    handleData("data/kleuren.json", showKleuren);
}
//#endregion

//#region ***  Event Listeners - listenTo___ ***
function listenToClickKleur(){
    const buttons = document.querySelectorAll(".js-kleurelement");
    for(const btn of buttons){
        btn.addEventListener("click", function() {
            const gekozenCode = this.getAttribute("data-code");
            const gekozenCategorie = this.dataset.category;
            html_uitvoerHolder.innerHTML = `De gekozen kleur heeft een hex-waarde van ${gekozenCode} en behoort tot de categorie ${gekozenCategorie}`;
        })
    }
}
//#endregion

//#region ***  INIT / DOMContentLoaded  ***
function init() {
    html_kleurenHolder = document.querySelector(".js-kleuren");
    html_uitvoerHolder = document.querySelector(".js-uitvoer");

    if (html_kleurenHolder) {
        getKleuren();
    }

    console.log("Dom loaded");
}
document.addEventListener("DOMContentLoaded", init);
//#endregion
