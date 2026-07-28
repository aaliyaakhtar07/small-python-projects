#Rock Paper Scissors Game
import random
emojis = {"r": "🪨", "p": "📄", "s": "✂️"}
choices = ("r", "p", "s")

while True: 
    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please choose 'r', 'p', or 's'.")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}.")
    print(f"Computer chose {emojis[computer_choice]}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif ((user_choice == "r" and computer_choice == "s") or 
        (user_choice == "p" and computer_choice == "r") or 
        (user_choice == "s" and computer_choice == "p")):
        print("You win!")
    else:
        print("Computer wins!")

    should_continue = input("Do you want to play again? (y/n): ").lower()
    if should_continue == "n":
        print("Thanks for playing!")
        break

