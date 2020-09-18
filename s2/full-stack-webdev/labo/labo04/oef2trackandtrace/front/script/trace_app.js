"use strict";

let htmlSearchText,
    htmlSearchBtn,
    htmlSectionInfoSender,
    htmlSectionTrackAndTrace,
    htmlStepDropOff,
    htmlStepWarehouse,
    htmlStepOutForDel,
    htmlStepDel,
    htmlStepDropOffDate,
    htmlStepWarehouseDate,
    htmlStepOutForDelDate,
    htmlStepDelDate,
    htmlSenderName,
    htmlSEnderPostcode;

function callbackVerwerkStatus(jsonObject) {
    console.log(jsonObject);
    //maak section zichtbaar
    htmlSectionInfoSender.classList.remove("u-hide");
    htmlSectionTrackAndTrace.classList.remove("u-hide");
    htmlSenderName.innerHTML = jsonObject.detail.naam;
    htmlSEnderPostcode.innerHTML = jsonObject.detail.postcode;

    htmlStepDropOffDate.innerHTML = jsonObject.detail.afgifte;
    htmlStepWarehouseDate.innerHTML = jsonObject.detail.sorteercentrum;
    htmlStepOutForDelDate.innerHTML = jsonObject.detail.onderweg;
    htmlStepDelDate.innerHTML = jsonObject.detail.bezorgd;
}

function callbackErrorStatus(response) {
    if (response && response.status == 404) {
        console.log(response);
        htmlSectionInfoSender.classList.add("u-hide");
        htmlSectionTrackAndTrace.classList.add("u-hide");
        htmlSearchText.value = "";
        htmlSearchText.placeholder = "geen geldig postpakket code";
    }
}

function showTrackAndTraceInfo() {
    //welk id?
    let id = htmlSearchText.value;
    let url = `http://localhost:5000/api/v1/trace/${id}`;
    //maak verbinding met API
    handleData(url, callbackVerwerkStatus, callbackErrorStatus);
}

document.addEventListener("DOMContentLoaded", function() {
    console.info("DOM geladen");
    htmlSearchText = document.querySelector(".js-search-txt");
    htmlSearchBtn = document.querySelector(".js-search-btn");
    htmlSectionInfoSender = document.querySelector(".js-section-info-sender");
    htmlSectionTrackAndTrace = document.querySelector(".js-section-trace");
    htmlStepDropOff = document.querySelector(".js-step-drop-off");
    htmlStepWarehouse = document.querySelector(".js-step-warehouse");
    htmlStepOutForDel = document.querySelector(".js-step-out-for-delivery");
    htmlStepDel = document.querySelector(".js-step-delivered");
    htmlStepDropOffDate = document.querySelector(".js-step-drop-off-datum");
    htmlStepWarehouseDate = document.querySelector(".js-step-warehouse-datum");
    htmlStepOutForDelDate = document.querySelector(".js-step-out-for-delivery-datum");
    htmlStepDelDate = document.querySelector(".js-step-delivered-datum");
    htmlSenderName = document.querySelector(".js-sender-name");
    htmlSEnderPostcode = document.querySelector(".js-sender-postcode");

    htmlSearchBtn.addEventListener("click", showTrackAndTraceInfo);
});
