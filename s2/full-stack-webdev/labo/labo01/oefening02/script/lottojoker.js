"use strict";

const zodiac = [
    "boogschutter",
    "kreeft",
    "leeuw",
    "maagd",
    "ram",
    "schorpioen",
    "steenbok",
    "stier",
    "tweelingen",
    "vissen",
    "waterman",
    "weegschaal"
];

function init() {
    let jsResult = document.querySelector(".js-result");
    const joker = generateJoker(3, 3);
    jsResult.innerHTML = showWinningNumbers(joker);
}

function generateJoker(aantalCijfers, aantalDieren) {
    let a = [];
    for (let c = 0; c < aantalCijfers; c++) {
        a.push(randomNumber(9));
    }

    for (let d = 0; d < aantalDieren; d++) {
        let rand = randomNumber(zodiac.length - 1);
        a.push(zodiac[rand]);
    }
    return a;
}

function showWinningNumbers(joker) {
    let html = '';
    for (let j of joker) {
        let div = document.createElement('div');
        if (typeof j == 'number') {
            div.innerHTML = j;
        } else {
			let image = document.createElement('img');
			image.setAttribute('src', 'images/zodiac/' + j + '.png');
			div.append(image);
		}
		html += div.outerHTML;
	}
	return html;
}

function randomNumber(max) {
    return Math.floor(Math.random() * (max + 1));
}

init();
