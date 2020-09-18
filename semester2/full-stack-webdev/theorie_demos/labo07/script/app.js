"use strict";

const functie_die_ik_op_elke_pagina_nodig_heb = function(message) {
  document.querySelector("body").innerHTML += `${message}`;
};

const functie_die_ik_enkel_op_pagina1_nodig_heb = function() {
  functie_die_ik_op_elke_pagina_nodig_heb("ik word uitgevoerd op pagina 1");
};

const functie_die_ik_enkel_op_pagina2_nodig_heb = function() {
  functie_die_ik_op_elke_pagina_nodig_heb("ik word uitgevoerd op pagina 2");
};

const init = function() {
  if (document.querySelector(".js-pagina1")) {
    functie_die_ik_enkel_op_pagina1_nodig_heb();
  } else {
    if (document.querySelector(".js-pagina2")) {
      functie_die_ik_enkel_op_pagina2_nodig_heb();
    }
  }
};

window.addEventListener("DOMContentLoaded", init);
