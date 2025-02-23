document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript Loaded!");
    
    let form = document.querySelector("form");
    
    if (form) {
        form.addEventListener("submit", function(event) {
            let inputs = form.querySelectorAll("input");
            let valid = true;

            inputs.forEach(input => {
                if (input.value.trim() === "") {
                    valid = false;
                    alert("All fields are required!");
                }
            });

            if (!valid) {
                event.preventDefault();
            }
        });
    }
});





document.addEventListener("visibilitychange", function() {
    if (document.hidden) {
        alert("Tab switching detected! Your exam session may be terminated.");
        fetch("/record_violation", { method: "POST" });
    }
});



function adminLogin() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    fetch("/admin/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.admin_id) {
            localStorage.setItem("admin_id", data.admin_id);
            alert("Login Successful");
            window.location.href = "/admin_dashboard.html";
        } else {
            alert("Invalid Credentials");
        }
    });
}
