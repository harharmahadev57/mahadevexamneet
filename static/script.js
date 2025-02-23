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





from models import Admin

@app.route("/admin_login", methods=["POST"])
def admin_login():
    data = request.json
    admin = Admin.query.filter_by(email=data["email"], password=data["password"]).first()
    if admin:
        login_user(admin)
        return jsonify({"message": "Admin Logged In"}), 200
    return jsonify({"error": "Invalid Credentials"}), 401
