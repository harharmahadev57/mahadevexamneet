document.getElementById('admin-login-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const adminId = document.getElementById('admin-id').value;
    const adminPassword = document.getElementById('admin-password').value;

    // Dummy check (Replace with actual authentication logic)
    if (adminId === "admin" && adminPassword === "admin123") {
        window.location.href = "admin-dashboard.html";  // Redirect to Admin Dashboard
    } else {
        alert("Invalid credentials!");
    }
});
