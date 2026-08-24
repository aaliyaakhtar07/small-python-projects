#Quiz Game
def run_quiz():
    questions = [
        {
            "prompt": "What is the correct file extension for Python files?",
            "options": ["A. .pt", "B. .pyt", "C. .py", "D. .pw"],
            "answer": "C",
        },
        {
            "prompt": "Which keyword is used to create a function in Python?",
            "options": ["A. function", "B. def", "C. fun", "D. create"],
            "answer": "B",
        },
        {
            "prompt": "What data type is the result of 3 / 2 in Python 3?",
            "options": ["A. int", "B. float", "C. double", "D. string"],
            "answer": "B",
        },
        {
            "prompt": "Which collection type is ordered, changeable, and allows duplicate members?",
            "options": ["A. Dictionary", "B. Set", "C. Tuple", "D. List"],
            "answer": "D",
        },
    ]

    score = 0

    print("=== Welcome to the Python Quiz Game! ===\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['prompt']}")
        for option in q["options"]:
            print(f"  {option}")

        # Get and validate user input
        while True:
            user_answer = (
                input("Your answer (A/B/C/D): ").strip().upper()
            )
            if user_answer in ["A", "B", "C", "D"]:
                break
            print("Invalid selection. Please choose A, B, C, or D.")

        # Check answer
        if user_answer == q["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! The correct answer was {q['answer']}.\n")

    # Display final results
    total = len(questions)
    percentage = (score / total) * 100
    print("=== Final Results ===")
    print(f"Score: {score}/{total} ({percentage:.0f}%)")

    if score == total:
        print("Perfect score! Excellent work.")
    elif score >= total / 2:
        print("Good job! Keep practicing.")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    run_quiz()