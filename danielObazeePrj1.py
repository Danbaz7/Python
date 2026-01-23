# Author: Daniel Obazee
# INF360 Programming with Python
print('Welcome to python basics')
userInput= input("What is your name: ")
print("Welcome" + " " + userInput)
print("Your name is "+ str(len(userInput)) + " characters long including any blank space(s)")
print(" ")

print('The next values entered will be used to test mathematical operators')
userValue1= int(input("Enter a number: "))
userValue2= int(input("Enter another number: "))

print("First number multiplied by second number is -- " + str((userValue1 * userValue2)))
print("First number added to the second number is -- " + str((userValue1 + userValue2)))
print("The remainder of the first number divided by 2 is -- " + str((userValue1 % 2)))
print("The remainder of the second number divided by 2 is -- " + str((userValue2 % 2)))

