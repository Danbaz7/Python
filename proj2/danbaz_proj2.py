# INF360 - Programming in Python

# Assignment 2



# Program 3: Treasure Door Challenge
# Uses comparison operators, boolean operators, if/elif/else,
# while loop with break/continue, , and random.randint()

import random

print(' ')
print("Welcome to the Treasure Door Challenge!")

while True:
    print("Three doors stand before you...\n")
    door = input("Choose door 1, 2, or 3: ")

    # comparison + boolean operator
    if door == "1":
        print("You found a sleeping dragon!")
    elif door == "2":
        print("You found a pile of gold!")
    elif door == "3":
        print("You found a mysterious chest!")
    else:
        print("Invalid door.")
        continue

    # random event
    event = random.randint(1, 3)

    if event == 1:
        print("A trap activates! You lose!\n")
    elif event == 2:
        print("You escape safely!\n")
    elif event == 3:
        print("You gain a magical item!\n")
    else:
        print("Something strange happens...")

    again = input("Play again? yes/no: \n")
    if again != "yes":
        break

print('***** TREASURES FOUND *****\n')
treasures = ["gold coin", "ruby", "emerald", "silver ring", "magic scroll", "ancient key"]
for i in range(5):
    reward = random.choice(treasures)
    print(f"You found a {reward}!")
