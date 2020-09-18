'use strict';

let url = "http://api.tvmaze.com/singlesearch/shows?q=Homeland&embed=episodes";

function toonData(data){
    console.log(`De naam van de serie is ${data.name}`);
    console.log(`Het uur waarop het wordt uitgezonden is ${data.schedule.time}`);
    console.log("Volgende genres:");
    for(let genre of data.genres){
        console.log(genre);
    }
    console.log("Overzicht episodes");
    for(let episode of data._embedded.episodes){
        console.log(`s ${episode.season} e ${episode.number} - ${episode.name}`);
    }
}

function getData(){
    console.log("Test");
    fetch(url).then(function(response) {
        if(!response.ok){
            console.log('response niet OK');
            throw Error(`Er is een probleem bij het fetchen: ${response.status}`);
        } else {
            return response.json();
        }
    })
    .then(json => toonData(json))
    .catch(error => console.error(`Fout bij het verwerken: ${error}`));
}

document.addEventListener("DOMContentLoaded", getData);