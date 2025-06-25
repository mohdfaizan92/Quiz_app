from db_config import get_connection

def register_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
        conn.commit()
    except:
        print("Welcome back,", username + "!")
    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    user_id = cursor.fetchone()[0]
    conn.close()
    return user_id

def fetch_questions():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    conn.close()
    return questions

def store_score(user_id, score, total_questions):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO scores (user_id, score, total_questions) VALUES (%s, %s, %s)",
        (user_id, score, total_questions)
    )
    conn.commit()
    conn.close()

def start_quiz(user_id):
    questions = fetch_questions()
    score = 0

    for q in questions:
        print("\n" + q['question'])
        print("A. " + q['option_a'])
        print("B. " + q['option_b'])
        print("C. " + q['option_c'])
        print("D. " + q['option_d'])
        ans = input("Your answer (A/B/C/D): ").upper()
        if ans == q['correct_option']:
            score += 1

    print("\nYou scored", score, "out of", len(questions))
    store_score(user_id, score, len(questions))

def main():
    username = input("Enter your username: ")
    user_id = register_user(username)
    start_quiz(user_id)

if __name__ == "__main__":
    main()



