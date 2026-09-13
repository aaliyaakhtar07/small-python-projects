#Banking Program
def show_balance():
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount<0:
        print("Please enter a valid amount.")
    else:
        return amount

def withdraw():
    pass

balance = 0
is_running = True

while is_running:
    print("Welcome to the Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ") 
    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Banking Program. Goodbye!")
