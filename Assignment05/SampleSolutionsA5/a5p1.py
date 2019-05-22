# define functions

def capitalize_every_2nd(s):
    ret_str = ""
    for count, ch in enumerate(s):
        if count % 2 == 0: 
            ret_str += ch.upper()
        else:
            ret_str += ch.lower()
    return ret_str

# main program
print(capitalize_every_2nd("Hello")) # should print HeLlO
print(capitalize_every_2nd("HEllo")) # should print HeLlO
print(capitalize_every_2nd("HellO")) # should print HeLlO
print(capitalize_every_2nd("hello world")) # should print HeLlO WoRlD"
