# Class04 Assignment04

## Part01

Write a number guessing program where the program generates a random number between 1 and 5. The user get's three guesses. If the guess is correct, the print a congratulatory message, otherwise, if there are still guesses left, print an encouraging message for them to try again. If they do not guess the number after three guesses, tell them they suck at this guessing game. 

NOTE: You can generate random numbers in Python. The code below prints to the screen a random integer between (inclusive) 0 and 5. The last line prints a number between 1 and 10 inclusive.

```python
import random

print(random.randint(0,5))
print(random.randint(1,10))

```

## Part02:

Write a program that asks a user to input a number equal to or less than 100. If the user enters a number that is outside this range, then print to the screen “ERROR: Input out of range” and ask the user to input another number. Otherwise, print the number they provided to the screen.


### Part03:

Write a program that asks for three numbers and prints “all the same” if they are all the same, “all different” if they are all different, and “neither” otherwise.


### Part04:


Water has a freezing point of 32 degrees, and a boiling point of 212 degrees. Write a program that asks a user to enter the water temperature in degrees and prints out if the water at this temperature is frozen, liquid, or gaseous (steam).

##  Part05

post your C04EX04 here.

## Challenge...

Create a copy of your NameWriter.py program, call it PrintWriter.py. Update PrintWriter.py to contain a function for each letter of your initials (if your initials have less than three unique letters, be sure to add another letter of your choice -- you should have three functions that print three unique letters). Name these functions whatever you wish. This function should accept an "anchor" starting x, y, and heading so that when calling the function you can specify where on the screen it will be drawn, and at what orientation.

Create a main method, and use these functions to draw a word on the screen. The word can be any sequence of the three characters (as you may not be able to create an english word from your initials). It's best if this word uses at least one of the letters multiple times.

This is not a mandatory assignment. Do it as a "challenge" if you wish.
