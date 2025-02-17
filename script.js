document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const studentId = document.getElementById('student-id').value;
    const studentPassword = document.getElementById('student-password').value;

    // Dummy check (replace with Firebase or MySQL authentication)
    if (studentId === "123" && studentPassword === "password") {
        document.querySelector('.login-container').style.display = "none";
        document.querySelector('.exam-container').style.display = "block";
    } else {
        alert("Invalid login credentials!");
    }
});

document.getElementById('exam-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const answers = {
        q1: document.querySelector('input[name="q1"]:checked')?.value,
        q2: document.querySelector('input[name="q2"]:checked')?.value,
    };

    // Submit answers to the server (Firebase, MySQL, etc.)
    alert("Your answers: " + JSON.stringify(answers));
    // Redirect to result page or show message
});
