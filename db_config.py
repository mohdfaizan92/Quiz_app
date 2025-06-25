import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="quizuser",
        password="QuizPassword123",
        database="quiz_app"
    )

