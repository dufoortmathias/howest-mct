"use strict";

const url =
    "https://opendata.arcgis.com/datasets/413c00cfda8743fbb94ce7e7e67d67c7_49.geojson";

/* STAP 2: Schrijf een loadData functie die - via FETCH - communiseert met de API */
function laadDataAfvalContainers() {
    fetch(url)
        .then(function(response) {
            if (!response.ok) {
                console.log("response niet OK");
                throw Error(
                    `Er is een probleem bij het fetchen: ${response.status}`
                );
            } else {
                return response.json();
            }
        })
        .then(json => verwerkAfvalContainers(json))
        .catch(error => console.error(`Fout bij het verwerken: ${error}`));
}

function zeroToStreepke(getal){
    if(getal == 0){
        return '--';
    }
    return getal;
}
/* STAP 3: Als fetch gelukt is, wordt deze functie uitgevoerd om de data via INNERHTML te tonen */
function verwerkAfvalContainers(data) {
    let afvalZuilen = data.features;
    let htmlContainer = document.querySelector(".js-placeholder");
    for (const item of afvalZuilen) {
        const straat = item.properties.STRAATNAAM;
        const tempREST = zeroToStreepke(item.properties.AANTAL_CNTR_REST);
        const tempGFT = zeroToStreepke(item.properties.AANTAL_CNTR_GFT);
        const tempPK = zeroToStreepke(item.properties.AANTAL_CNTR_PK);
        const tempPMD = zeroToStreepke(item.properties.AANTAL_CNTR_PMD);
        const tempGLAS = zeroToStreepke(item.properties.AANTAL_CNTR_GLAS);

        const innerHTML = `<article class="c-locatie">
        <div class="c-locatie__adres">${straat}</div>
        <div class="c-locatie__info">
          <div class="c-locatie__type">
            GFT
            <div class="c-locatie__aantal">${tempGFT}</div>
          </div>
          <div class="c-locatie__type">
            GLAS
            <div class="c-locatie__aantal">${tempGLAS}</div>
          </div>
          <div class="c-locatie__type">
            PMD
            <div class="c-locatie__aantal">${tempPMD}</div>
          </div>
          <div class="c-locatie__type">
            REST
            <div class="c-locatie__aantal">${tempREST}</div>
          </div>
          <div class="c-locatie__type">
            PAPIER
            <div class="c-locatie__aantal">${tempPK}</div>
          </div>
        </div>
      </article>`;
        htmlContainer.innerHTML += innerHTML;
    }
}

/* STAP 1: Voeg DOMContentLoaded Event Listener toe  */
document.addEventListener("DOMContentLoaded", laadDataAfvalContainers);
