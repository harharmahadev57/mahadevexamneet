CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    class VARCHAR(20) NOT NULL,
    group_name VARCHAR(20)
);

CREATE TABLE exams (
    id SERIAL PRIMARY KEY,
    exam_name VARCHAR(100) NOT NULL,
    exam_date TIMESTAMP NOT NULL,
    question_paper TEXT NOT NULL,
    answer_key TEXT NOT NULL
);

CREATE TABLE results (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id) ON DELETE CASCADE,
    exam_id INT REFERENCES exams(id) ON DELETE CASCADE,
    marks INT NOT NULL,
    total_marks INT NOT NULL,
    result_status VARCHAR(10) CHECK (result_status IN ('Pass', 'Fail'))
);
