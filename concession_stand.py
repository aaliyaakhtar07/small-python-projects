#Concesssion Stand Program
menu = {"pizza": 5.00, "hot dog": 3.00, "soda": 1.50, "candy": 2.00, "popcorn": 4.00, "nachos": 4.50, "ice cream": 3.50, "pretzel": 2.50, "water": 1.00, "coffee": 2.00}
cart = []
total = 0
print("----------MENU----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")
while True:
    item = input("Enter an item to add to your cart (or type 'done' to finish): ").lower()
    if item.lower() == "done":
        break
    elif item in menu:
        cart.append(item)
        total += menu[item]
        print(f"{item} added to cart. Current total: ${total:.2f}")
    else:
        print("Item not found in menu. Please try again.")
print(cart)
print(f"Your total is: ${total:.2f}")