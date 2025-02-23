const fetch = require("node-fetch");

fetch("https://mahadevexamneet-5.onrender.com/admin", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email: "karan57@gmail.com", password: "k1234" })
})
.then(res => res.json())
.then(data => console.log(data))
.catch(err => console.error("Error:", err));
