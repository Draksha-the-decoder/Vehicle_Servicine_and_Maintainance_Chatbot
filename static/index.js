function getBotResponse() {
    var rawText = document.getElementById("textInput").value;
    console.log(rawText);
    var userHtml = '<p class="userText">' + rawText + '</p>';
    document.getElementById("chat").innerHTML += userHtml;
    document.getElementById("chat").scrollTop = document.getElementById("chat").scrollHeight;
    document.getElementById("textInput").value = "";

    // $.get("/get", { msg: rawText }).done(function (data) {
    //     var botHtml = '<p class="botText">' + data + '</p>';
    //     document.getElementById("chat").innerHTML += botHtml;
    //     document.getElementById("chat").scrollTop = document.getElementById("chat").scrollHeight;
    // });
    fetch('/get?msg=rawText')
                .then(response => response.text())
                .then(data => {
                    const botHtml = '<p class="botText">' + data + '</p>';
                    const chatElement = document.getElementById("chat");
                    chatElement.innerHTML += botHtml;
                    chatElement.scrollTop = chatElement.scrollHeight;
                })
                .catch(error => console.error('Error fetching data:', error));
       
}