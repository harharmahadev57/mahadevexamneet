// Student Login Logic
document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const studentId = document.getElementById('student-id').value;
    const studentPassword = document.getElementById('student-password').value;

    if (studentId === "student1" && studentPassword === "password123") {
        window.location.href = "student-dashboard.html";  // Redirect to Student Dashboard
    } else {
        alert("Invalid credentials!");
    }
});

// Admin Login Logic
document.getElementById('admin-login-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const adminId = document.getElementById('admin-id').value;
    const adminPassword = document.getElementById('admin-password').value;

    if (adminId === "admin" && adminPassword === "admin123") {
        window.location.href = "admin-dashboard.html";  // Redirect to Admin Dashboard
    } else {
        alert("Invalid admin credentials!");
    }
});

// Exam Submission Logic (for student)
document.getElementById('exam-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const answers = {
        q1: document.querySelector('input[name="q1"]:checked')?.value,
    };

    alert("Your answers: " + JSON.stringify(answers));
});
