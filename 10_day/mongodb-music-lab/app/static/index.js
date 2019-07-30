function loadDoc() {
    // create a XMLHttpRequest object called req
    var req = new XMLHttpRequest();
    // this is the callback function:
    // upon receiving a response from the server, execute this
    req.onreadystatechange = function () {
        if (req.readyState == 4) { // if response received
            if (req.status != 200) { // if error(status code not 200)
                console.log(req.statusText); // outputs error msg
            } else { // if status code is 200
                console.log("success... executing success code");
                // JSON.parse parses JSON response into readable format
                var response = JSON.parse(req.responseText);
                console.log(response);
                // change the element
                document.getElementById("target").style.display = "block";
                document.getElementById("target").innerHTML = "Song added: " + response.output;
            }
        }
    }
    // begin steps to send ajax request
    // get the element value
    var un = document.getElementById("sName").value;
    var art = document.getElementById("sArt").value;
    var desc = document.getElementById("sDesc").value;
    // this is the query string, they start with a "?[insert key value]=[insert value]"
    var postVars = "sName=" + un + "&sArt=" + art + "&sDesc=" + desc;
    // console.log("sending this: " + un);
    // use setRequestHeader if POST method, and req.send(postVars)
    // if GET, add the postVars to the query string
    req.open("POST", "/ajax", true);
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    req.send(postVars);
    console.log("finished sending ajax request");
}