function init() {
    let jsHolder = document.querySelector(".js-holder");
    jsHolder.appendChild(createCountDown());
}

function createCountDown() {
    let counter = document.createElement("div");
    let size = 10;
    while (size != 0) {
        let span = document.createElement("span");
        span.innerHTML = size + "&nbsp;";
        span.style.fontSize = size + "em";
        if (size % 2 === 0) {
            span.classList.add("u-even");
        } else {
            span.classList.add("u-odd");
        }
        counter.append(span);
        size--;
    }
    console.log(counter);
    return counter;
}

function realCountDown() {
    const jsHolder = document.querySelector(".js-holder");
    let size = 10;

    const x = setInterval(() => {
        let span = document.createElement("span");
            span.innerHTML = size + "&nbsp;";
            span.style.fontSize = size + "em";
            if (size % 2 === 0) {
                span.classList.add("u-even");
            } else {
                span.classList.add("u-odd");
            }
            jsHolder.append(span);
            size--;
        if(size <= 0){
            clearInterval(x);
        }
    }, 100 );

}

// init();
realCountDown();
