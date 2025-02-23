import React from "react";

function App() {
    const loginUser = () => {
        fetch("https://mahadevexamneet-5.onrender.com/admin", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email: "karan57@gmail.com", password: "k1234" })
        })
        .then(res => res.json())
        .then(data => console.log(data))
        .catch(err => console.error("Error:", err));
    };

    return (
        <div>
            <h1>Login</h1>
            <button onClick={loginUser}>Login</button>
        </div>
    );
}

export default App;
