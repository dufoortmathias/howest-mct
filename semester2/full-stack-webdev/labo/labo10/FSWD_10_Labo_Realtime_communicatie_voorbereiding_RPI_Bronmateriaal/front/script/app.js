const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

const clearClassList = function (el) {
    el.classList.remove("c-room--wait");
    el.classList.remove("c-room--on");
};

const listenToUI = function () {
    let btns = document.querySelectorAll(".js-power-btn");
    for (let btn of btns) {
        btn.addEventListener("click", (e) => {
			let id = e.target.dataset.idlamp;
			let status = e.target.dataset.statuslamp;
			console.log('status bij click: ' + status)
			let nieuweStatus = null;
			if (status == 0){
				nieuweStatus = 1;
			} else {
				nieuweStatus = 0;
			}
            const room = document.querySelector(`.js-room[data-idlamp="${id}"]`);
            clearClassList(room);
            room.classList.add("c-room--wait");
            socket.emit("F2B_switch_light", { lamp_id: id, new_status: nieuweStatus });
        });
    }
};

const listenToSocket = function () {
    socket.on("connected", () => {
        console.log("Verbonden met socket webserver.");
    });

    socket.on("B2F_status_lampen", (jsonObject) => {
        console.log("Dit is de status van de lampen");
        console.log(jsonObject);
        for (const lamp of jsonObject.lampen) {
            const room = document.querySelector(`.js-room[data-idlamp="${lamp.id}"]`);
            if (room) {
                const knop = room.querySelector(".js-power-btn");
                knop.setAttribute("data-statuslamp", lamp.status);
                clearClassList(room);
                if (lamp.status == 1) {
                    room.classList.add("c-room--on");
                }
            }
        }
    });

    socket.on("B2F_verandering_lamp", (jsonObject) => {
        console.log("Dit is de status van de veranderde lamp");
        console.log(jsonObject);
		const lamp = jsonObject.lamp;
		const status = jsonObject.status;
        const room = document.querySelector(`.js-room[data-idlamp="${lamp}"]`);
        if (room) {
            const knop = room.querySelector(".js-power-btn");
            knop.setAttribute("data-statuslamp", status);
            clearClassList(room);
            if (status == 1) {
                room.classList.add("c-room--on");
            }
        }
	});
	
	socket.on("B2F_alles_uit", jsonObject => {
		console.log("Alle lampen uit");
		console.log(jsonObject);
	});
};

document.addEventListener("DOMContentLoaded", function () {
    console.info("DOM geladen");
    listenToUI();
    listenToSocket();
});
