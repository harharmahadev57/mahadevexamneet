def create_tables():
    cursor = mysql.connection.cursor()
    
    # Students Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone_number VARCHAR(15) NOT NULL,
        email VARCHAR(100) NOT NULL,
        std VARCHAR(10) NOT NULL,
        class VARCHAR(50) NOT NULL,
        student_group VARCHAR(20) NOT NULL
    )
    """)
    
    # Admin Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    )
    """)

    # Exams Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exams (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        pdf_link VARCHAR(255) NOT NULL
    )
    """)

    mysql.connection.commit()
    cursor.close()
