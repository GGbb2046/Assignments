"""
Author:         Tim Smith
Description:    Assignment03 part2 sample solution
"""

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

# there are two general ways we could build this if/elif/else structure

# this is the way it is done in most languages


if x==y and x==z:
    print("All the same")
elif x!=y and y!=z and x!=z:
    print("All different")
else:
    print("Neither")

# this way is rather unique to python, but "pythonic"
if x == y == z:
    print("All the same")
elif x != y != z:
    print("All different")
else:
    print("Neither")