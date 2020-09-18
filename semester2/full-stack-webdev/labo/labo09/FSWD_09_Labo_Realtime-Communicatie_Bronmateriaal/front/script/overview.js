"use strict";

const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

function callbackWissenGelukt() {
    console.log("Wissen gelukt");
}

function showTableData(data) {
    const table = document.querySelector(".js-table");
    let tableHTML = `<tr class="c-row is-header">
    <th class="c-cell">Date</th>
    <th class="c-cell">Amount</th>`;
    for (const row of data) {
        tableHTML += `
        <tr class="c-row">
            <td class="c-cell">${row.date}</td>
            <td class="c-cell">${row.amount}</td>    
        </tr>`;
    }
    table.innerHTML = tableHTML;
}

function listenToUI() {
    document.querySelector(".js-clear-amount-today").addEventListener("click", () => {
        handleData(`http://${lanIP}/api/v1/progress/today`, callbackWissenGelukt, null, "DELETE");
    });
}

function listenToSocket() {
    socket.on("B2F_addProgress", () => {
        getProcessData();
    });

    socket.on("B2F_clear", () => {
        getProcessData();
    });
}

function getProcessData() {
    handleData(`http://${lanIP}/api/v1/progress`, showTableData, null, "GET");
}

function init() {
    listenToUI();
    listenToSocket();
    getProcessData();
}

document.addEventListener("DOMContentLoaded", () => {
    init();
});
