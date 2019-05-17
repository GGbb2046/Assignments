"""
Author:         Tim Smith
Description:    Assignment03 part1 sample solution
"""

while True:
    x = int(input("Please enter a number that is less than 100: "))
    if x < 100:
        print("Good job. You are a compliant user that follows instructions well.")
        break
    else:
        print("Error: Out of range")