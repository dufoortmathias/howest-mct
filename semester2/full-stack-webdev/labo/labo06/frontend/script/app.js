"use strict";

let currentDestinationID;

//#region ***  DOM references ***
let html_destinationHolder, html_destinationSelect, html_routeHolder, html_selectedCity, html_adaptTrain;
//#endregion

//#region ***  Callback-Visualisation - show___ ***
function showDestinations(jsonObject) {
    for (let bestemming of jsonObject.bestemmingen) {
        //toon menu
        html_destinationHolder.innerHTML += `<li class="c-sidebar-item"><button class="c-sidebar-button js-station" data-destination-id="${bestemming.idbestemming}">${bestemming.stad}</button></li>`;
        //toon keuzelijst
        html_destinationSelect.innerHTML += `<option value="${bestemming.idbestemming}">${bestemming.stad}</option>`;
    }
    //luister naar click event van menu items
    listenToSelectStation();
}

function showTrainsByDestination(jsonObject) {
    html_routeHolder.innerHTML = "";
    for (let trein of jsonObject.treinen) {
        let vertraging = "-";
        if (trein.vertraging != null) {
            vertraging = trein.vertraging;
        }
        let afgeschaft = "";
        if (trein.afgeschaft) {
            afgeschaft = `<span class="c-traject__cancelled-label">afgeschaft</span>`;
        }
        html_routeHolder.innerHTML += `
        <div class="c-traject">
            <div class="c-traject__info">
                <h2 class="c-traject__name">${trein.stad}</h2>
                <p class="c-traject__train-id">Trein ${trein.idtrein}</p>
            </div>
            <div class="c-traject__departure">${trein.vertrek}</div>
            <div class="c-traject__track">${trein.spoor}</div>
            <div class="c-traject__delay">${vertraging}</div>
            <div class="c-traject__cancelled">${afgeschaft}</div>
            <div class="c-traject__updatevertraging">
                <a href="vertraging.html?TreinID=${trein.idtrein}">
                    <svg class="c-traject__updatevertraging-symbol" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="arcs">
                        <polygon points="16 3 21 8 8 21 3 21 3 16 16 3"></polygon>
                    </svg>
                </a>
            </div>
            <div class="c-traject__update">
                <a href="aanpassen.html?TreinID=${trein.idtrein}">
                    <svg class="c-traject__update-symbol" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="arcs">
                        <polygon points="16 3 21 8 8 21 3 21 3 16 16 3"></polygon>
                    </svg>
                </a>
            </div>
            <div class="c-traject__delete">
                <svg class="c-traject__delete-symbol" data-trein-id="${trein.idtrein}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="arcs">
                    <polyline points="3 6 5 6 21 6"></polyline>
                    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                    <line x1="10" y1="11" x2="10" y2="17"></line>
                    <line x1="14" y1="11" x2="14" y2="17"></line>
                </svg>
            </div>
        </div>`;
    }
    listenToDeleteButton();
}

//#endregion

//#region ***  Callback-No Visualisation - callback___  ***
const callbackAddTrain = function(data) {
    if (data.treinid > 0) {
        console.log("Added train");
        currentDestinationID = data.bestemming;
        getTrainsByDestination(currentDestinationID);
    }
};

const callbackRemoveTrain = function(data) {
    if (data.row_count > 0) {
        console.log("Removed train");
        getTrainsByDestination(currentDestinationID);
    }
};
//#endregion

//#region ***  Data Access - get___ ***
function getDestinations() {
    handleData("http://localhost:5000/api/v1/bestemmingen", showDestinations);
}

function getTrainsByDestination(destinationId) {
    handleData("http://localhost:5000/api/v1/treinen/bestemming/" + destinationId, showTrainsByDestination);
}
//#endregion

//#region ***  Event Listeners - listenTo___ ***
function listenToSelectStation() {
    let options = document.querySelectorAll(".js-station");

    for (let option of options) {
        option.addEventListener("click", function() {
            html_selectedCity.innerHTML = this.innerHTML;
            currentDestinationID = this.dataset.destinationId;
            getTrainsByDestination(currentDestinationID);
        });
    }

    //selecteer bij default de eerste bestemming, zodat de routeplanner nooit leeg is
    currentDestinationID = options[0].dataset.destinationId;
    getTrainsByDestination(currentDestinationID);
    html_selectedCity.innerHTML = options[0].innerHTML;
    
}

function listenToDeleteButton() {
    let buttons = document.querySelectorAll(".c-traject__delete-symbol");
    for (let button of buttons) {
        button.addEventListener("click", function() {
            handleData(
                `http://localhost:5000/api/v1/treinen/${this.dataset.treinId}`,
                callbackRemoveTrain,
                null,
                "DELETE"
            );
        });
    }
}

function listenToAddButton() {
    let button = document.querySelector(".js-add-train");
    button.addEventListener("click", function() {
        console.log(document.querySelector("#add_afgeschaft").checked);
        let jsonObject = {
            bestemming: html_destinationSelect.value,
            vertrek: document.querySelector("#add_vertrek").value,
            spoor: document.querySelector("#add_spoor").value,
            vertraging: document.querySelector("#add_vertraging").value,
            afgeschaft: document.querySelector("#add_afgeschaft").checked
        };
        handleData("http://127.0.0.1:5000/api/v1/treinen", callbackAddTrain, null, "POST", JSON.stringify(jsonObject));
    });
}
//#endregion

//#region ***  INIT / DOMContentLoaded  ***
const init = function() {
    console.log("🚂", "https://www.youtube.com/watch?v=8oVTXSntnA0");
    html_destinationHolder = document.querySelector(".js-destinations");
    html_routeHolder = document.querySelector(".js-trajects");
    html_selectedCity = document.querySelector(".js-departure");
    html_destinationSelect = document.querySelector(".js-destination");
    html_adaptTrain = document.querySelector(".js-adapttrain");

    if (html_destinationHolder) {
        getDestinations();
    }
    listenToAddButton();
};

document.addEventListener("DOMContentLoaded", () => {
    init();
});
//#endregion
