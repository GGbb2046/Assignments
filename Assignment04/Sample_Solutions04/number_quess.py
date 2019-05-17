import random

num = random.randint(1,5)
count = 0
while True:
    guess = int(input("Guess a number between 1 and 5:"))
    if guess==num:
        print("Congratulations")
        break
    elif count == 2:
        print("You suck at guessing numbers.")
        break
    else:
        print("Please try again")
    count = count +1
        