"""
Author:         Tim Smith
Description:    Assignment03 part1 sample solution
"""

temp = int(input("Please enter the temperature of the water in Fahrenheit: "))

if temp >= 212:
    print("Steam")
elif temp >= 32:
    print("Liquid")
else:
    print("Frozen")

