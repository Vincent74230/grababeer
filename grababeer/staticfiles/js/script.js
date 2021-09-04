var count = 1;
var prev = document.getElementById("previous");
var next = document.getElementById("next");
var disp = document.getElementById("display");


prev.onclick = function () {
    count--;
    disp.innerHTML = count;
}

prev.onclick = function () {
    count++;
    disp.innerHTML = count;
}