#Compound Interest Calculator
principle = 0
rate = 0
time = 0
while principle<=0:
    principle = float(input("Enter the principle amount: "))
    if principle<=0:
        print("Principle amount must be greater than 0. Please try again.")
while rate<=0:
    rate = float(input("Enter the interest rate: "))
    if rate<=0:
        print("Interest rate must be greater than 0. Please try again.")
while time<=0:
    time = float(input("Enter the time period in years: "))
    if time<=0:
        print("Time period must be greater than 0. Please try again.")
print("The compound interest is: ", principle * (1 + rate / 100) ** time - principle)
