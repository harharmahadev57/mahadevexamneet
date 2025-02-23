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
