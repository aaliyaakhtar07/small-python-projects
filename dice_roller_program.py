#Dice Roller Program
import random
print("Welcome to the Dice Roller Program!")
#● ┌ ─ ┐ │ └ ┘
"┌──────────┐"
"│          │"
"│          │"
"│          │"
"└──────────┘"
dice_art ={
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
}
dice = []
total = 0
num_of_dice = int(input("How many dice would you like to roll? "))
for i in range(num_of_dice):
    roll = random.randint(1, 6)
    dice.append(roll)
for line in range(5):
    for die in dice:
        print(dice_art[die][line], end=" ")
    print()