document.getElementById("encodeForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let formData = new FormData(this);

    fetch("/encode", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            return response.text().then(text => { throw new Error(text); });
        }
        return response.blob();
    })
    .then(blob => {
        let url = window.URL.createObjectURL(blob);
        let a = document.createElement("a");
        a.href = url;
        a.download = "encoded_image.png";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    })
    .catch(error => alert(error.message));
});

document.getElementById("decodeForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let formData = new FormData(this);

    fetch("/decode", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("decodedMessage").value = data.message;
    })
    .catch(error => alert("Error decoding message!"));
});

function toggleMessage() {
    let field = document.getElementById("decodedMessage");
    field.type = (field.type === "password") ? "text" : "password";
}
