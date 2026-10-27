'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr]

print(f"Computer chose {reverseDict[computer]}")
print(f"You chose {reverseDict[you]}")

if (computer == you):
    print("It's a tie!")
'''else:
    if (computer == -1 and you == 1) :
        print("You win!")
    elif (computer == -1 and you == 0):
        print("You lose!")
    elif (computer == 1 and you == -1):
        print("You win!")
    elif (computer == 1 and you == 0):
        print("You win!")
    elif (computer == 0 and you == -1):
        print("You win!")
    elif (computer == 0 and you == 1):
        print("You lose!")'''

if (computer-you == -1) or (computer-you == 2):
    print("You lose!")
else:
    print("You win!")