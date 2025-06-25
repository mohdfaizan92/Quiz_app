
CREATE DATABASE quiz_app;
USE quiz_app;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    option_a VARCHAR(100),
    option_b VARCHAR(100),
    option_c VARCHAR(100),
    option_d VARCHAR(100),
    correct_option CHAR(1)
);

CREATE TABLE IF NOT EXISTS scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    score INT,
    total_questions INT,
    quiz_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
USE quiz_app;

INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_option) VALUES
('What is the capital of France?', 'Berlin', 'London', 'Paris', 'Madrid', 'C'),
('Which language is used for data science?', 'Java', 'Python', 'C++', 'HTML', 'B'),
('Who invented the light bulb?', 'Newton', 'Edison', 'Einstein', 'Tesla', 'B');







