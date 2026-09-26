#Python Slot Machine
def spin_row():
    pass

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

if __name__ == "__main__":
    main()