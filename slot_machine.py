#Python Slot Machine
import random
def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]
    
def print_row(row):
    print("****************")
    print(" | ".join(row))
    print("****************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0
    
def main():
    balance = 100

    print("*********************************")
    print("Welcome to the Slot Machine Game!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*********************************")

    while balance > 0:
        print(f"Your current balance is ${balance}")
        bet = int(input("Please enter your bet amount (press 0 to quit): "))
        if bet == 0:
            break
        if bet > balance:
            print("You cannot bet more than your current balance!")
            continue
        if bet <= 0:
            print("Please enter a valid bet amount!")
            continue
        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"Congratulations! You won ${payout}!")
        else:
            print("Sorry, you didn't win this time.")
        balance += payout

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

    print("**********************************")
    print(f"Game Over! Your final balance is ${balance}")
    print("**********************************") 
if __name__ == "__main__":
    main()