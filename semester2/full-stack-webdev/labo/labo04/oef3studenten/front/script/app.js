'use strict';
let htmlSelectField; let htmlPlaceholder;

const callBackVerwerkStatus = function(jsonObject){
    let html =''
    const details = jsonObject.detail
    for(let i=0;i<details.length;i++){
        html += `<article class="c-resultaat"> 
                <div class="c-resultaat-module">${details[i].module}</div>`
        if(details[i].punt >= 10){
            html += `<div class="c-resultaat-punt c-resultaat__punt--geslaagd"> ${details[i].punt} </div></article>`
        }
        else{
            html += `<div class="c-resultaat-punt c-resultaat__punt--gebuisd"> ${details[i].punt}</div></article>`
        }
    }
    htmlPlaceholder.innerHTML = html
}

const callBackErrorStatus = function(response){
    if(response && response.status == 404){
        htmlPlaceholder.innerHTML = 'Geen Geldige Student'
    }
    else{
        htmlPlaceholder.value = 'Error'
    }
}


const showStudentInfo = function(){
    // const student = htmlSelectField.value; // Only for change event
    // indien je change gebruikt kan je gewoon de value uit de select halen. 
    const selectedIndex = this.selectedIndex;
    const arrOptions = this.options
    const selectedValue = arrOptions[selectedIndex].value;
    const url = `http://127.0.0.1:5000/api/v1/studenten/${selectedValue}`
    handleData(url, callBackVerwerkStatus, callBackErrorStatus);
}
const callBackVerwerkStudenten = function(jsonObject){
    
    let html ='<option value=""></option>'
    for(let i=0; i<jsonObject.length;i++){
        html += `<option value="${jsonObject[i]}">${jsonObject[i]}</option>`
    }
    htmlSelectField.innerHTML = html
}
const loadStudentNames = function(){
    const url = `http://127.0.0.1:5000/api/v1/studenten`
    handleData(url, callBackVerwerkStudenten, callBackErrorStatus);
}

document.addEventListener('DOMContentLoaded', function() {
  htmlSelectField = document.querySelector('.js-studenten');
  htmlPlaceholder = document.querySelector('.js-punten-placeholder');
  htmlSelectField.addEventListener('input', showStudentInfo);
  // Ipv een input event kan je ook change gebruiken
  loadStudentNames();
});
 