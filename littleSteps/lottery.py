import random
import sys

print("*" * 10, "Guess your lucky number", "*" * 10)
print(" " * 8, "Type 0 to exit if you wish.")
ticket = 1
win = 0
tries = 0

while ticket:
    tries += 1
    win = random.randrange(1, 11, 1)
    ticket = int(input("Your ticket number from 1 to 10: "))
    if ticket == 0:
        print("Good luck! See you soon!")
        break
    if ticket == win:
        print(f"Your ticket {ticket} is the winning ticket! Congratulations!")
        print(f"Your number of tries is {tries}.")
        sys.exit
    else:
        print(f"Sorry, the winning ticket is {win}. Better luck next time!")
