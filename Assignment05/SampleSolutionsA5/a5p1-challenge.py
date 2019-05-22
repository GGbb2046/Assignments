# define functions

def capitalize_every_2nd(s):
    return ''.join([ch.upper() if count%2==0 else ch.lower() for (count , ch) in enumerate(s)])

# main program
print(capitalize_every_2nd("Hello")) # should print HeLlO
print(capitalize_every_2nd("HEllo")) # should print HeLlO
print(capitalize_every_2nd("HellO")) # should print HeLlO
print(capitalize_every_2nd("hello world")) # should print HeLlO WoRlD"
