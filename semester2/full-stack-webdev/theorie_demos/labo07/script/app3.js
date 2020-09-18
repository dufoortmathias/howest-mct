"use strict";

const functie_die_ik_op_elke_pagina_nodig_heb = function(message) {
  document.querySelector(".js-result").innerHTML += `${message}<br/>`;
  console.log(message);
};
const doeIets = function(element) {
  functie_die_ik_op_elke_pagina_nodig_heb(element);
  element.innerHTML = "Hier heb ik reeds op geklikt.";
};
const doeIetsAnders = function(evt) {
  functie_die_ik_op_elke_pagina_nodig_heb(evt.target);
  functie_die_ik_op_elke_pagina_nodig_heb(evt.screenX);
};

const init = function() {
  let items = document.querySelectorAll(".c-container__item");

  for (const item of items) {
    item.addEventListener("click", function(e) {
      //gebruik van this
      doeIets(this);
      //gebruik van het event
      doeIetsAnders(e);
    });
  }
};

window.addEventListener("DOMContentLoaded", init);
