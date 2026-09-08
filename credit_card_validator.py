#Credit Card Validator
sum_odd_digits = 0
sum_even_digits = 0
total = 0
card_number = input("Enter your credit card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
print(f"Card Number: {card_number}")
