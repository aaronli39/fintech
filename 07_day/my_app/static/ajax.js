function loadDoc() {
    console.log("changing visibility");

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            ele = document.getElementById("ajax");
            ele.style.visbility = "visible";
            ele.innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "ajax", true);
    xhttp.send();
}
