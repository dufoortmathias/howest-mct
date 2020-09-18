"use strict";

let html_addButton, html_wave, html_percentage, html_logWater;
const dailyGoal = 1500;
let currentProgress = 0; // in milliliter
const lanIP = `${window.location.hostname}:5000`; //ppublic ip van de webserver
const socket = io(lanIP);

function updateView(value) {
    html_percentage.innerHTML = value;
    html_wave.style.transform = `translateY(${100 - value}%)`;
}

function listenToUI() {
    let html_waterAmount = document.querySelectorAll(".js-water-amount");
    for (let box of html_waterAmount) {
        box.addEventListener("change", (e) => {
            let amount = box.getAttribute("data-amount");
            document.querySelector(".js-log").innerHTML = amount;
            html_addButton.setAttribute("data-amount", amount);
        });
    }

    html_addButton.addEventListener("click", () => {
        const newAmount = html_addButton.dataset.amount
        console.log(`Er wordt ${newAmount} ml gedronken`);
        socket.emit("F2B_new_logging", { amount: newAmount });
    });
}

function listenToSocket() {
    socket.on("connected", () => {
        console.log("verbonden met socket");
    });

    socket.on("B2F_connected", value => {
        const progressInPercentage = Math.ceil(currentProgress / dailyGoal * 100);
        currentProgress = value.currentProgress;
        updateView(progressInPercentage);
    });

    socket.on('B2F_addProgress', value => {
        currentProgress += parseInt(value.amount);
        const progressInPercentage = Math.ceil((currentProgress / dailyGoal) * 100);
        updateView(progressInPercentage);
    })

    socket.on("B2F_clear", (value) => {
        currentProgress = parseInt(value.amount);
        const progressInPercentage = Math.ceil((currentProgress / dailyGoal) * 100);
        updateView(progressInPercentage);
    });
}

function init() {
    html_addButton = document.querySelector(".js-log-water");
    html_wave = document.querySelector(".js-waves");
    html_percentage = document.querySelector(".js-percentage");
    document.querySelector(".js-goal").innerHTML = dailyGoal;

    listenToUI();
    listenToSocket();
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("Dom Content loaded.");
    init();
});
