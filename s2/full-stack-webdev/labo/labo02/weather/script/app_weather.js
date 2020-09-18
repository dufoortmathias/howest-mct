"use strict";

const url =
    "https://api.openweathermap.org/data/2.5/forecast?q=kortrijk,BE&appid=5ab3cf66921da480525dffd751748008&units=metric&lang=nl";

/* STAP 2 */
function init() {
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
        .then(json => verwerkWeer(json))
        .catch(error => console.error(`Fout bij het verwerken: ${error}`));
}

/* STAP 3 */
function weatherCodeToImage(weerCode) {
    let codeString = weerCode.toString();
    let eersteDigit = codeString.substring(0, 1);
    let dict = {
        2: "wi-thunderstorm.svg",
        3: "wi-sprinkle.svg",
        5: "wi-rain.svg",
        6: "wi-snow.svg",
        7: "wi-fog.svg",
        8: "wi-fog.svg",
        7: "wi-fog.svg",
        7: "wi-fog.svg",
        7: "wi-fog.svg"
    };
}

function dagNrNaarNaam(nummer){
    const arr = ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag'];
    return arr[nummer];
}

function verwerkWeer(json) {
    const locatie = json.city.name;
    console.log(locatie);
    const voorspellingen = json.list;
    console.log(voorspellingen);
    const htmlCity = document.querySelector(".js-city-placeholder");
    const htmlVoorspelling = document.querySelector(".js-weather-placeholder");

    htmlCity.innerHTML = locatie;
    htmlVoorspelling.innerHTML = "";

    // vul voorspellingen in (lus -> maar maak sprongen van 8 (3x8 = 24u))
    for (let i = 0; i < voorspellingen.length; i += 8) {
        const huidigeVoorspelling = voorspellingen[i];
        const max = Math.round(huidigeVoorspelling.main.temp_max);
        const weerType = huidigeVoorspelling.weather[0].description;
        const weerTypeEngels = huidigeVoorspelling.weather[0].main;
        const min = Math.round(huidigeVoorspelling.main.temp_min);

        const element = huidigeVoorspelling;
        const datumUtc = element.dt;
        const dag = new Date(datumUtc * 1000);
        const dagNummer = dag.getDay();
        const dagNaam = dagNrNaarNaam(dagNummer - 1);
        

        const dagHTML = `<div class="c-forecast">
        <div class="c-forecast__datum">${dagNaam}</div>
        <div class="c-forecast__symbol">
          <img src="images/weather/wi-${weerTypeEngels.toLowerCase()}.svg" alt="${weerType}" />
        </div>
        <div class="c-forecast__uitleg">
          ${weerType}
        </div>
        <div class="c-forecast__max">${max}°C</div>
        <div class="c-forecast__min">${min}°C</div>
      </div>`;
        htmlVoorspelling.innerHTML += dagHTML;
    }
}

/* STAP 1 */
document.addEventListener("DOMContentLoaded", init);
