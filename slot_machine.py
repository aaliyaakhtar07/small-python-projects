#Python Slot Machine
import random
def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]
    
def print_row():
    pass

def get_payout():
    pass

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

if __name__ == "__main__":
    main()