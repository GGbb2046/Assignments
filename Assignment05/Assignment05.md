# Assignment #5

## Part 1

Create and test a function that accepts a string and returns a string with every second letter capitalized (starting with the first), and all other characters lowercase. As a challenge, write the function body using one line of code.


# Part 2

Create a a command line encrypt/decrypt program called crypt.py. Use the encrypt decrypt scheme covered in class05. 

The program should do the following:

To print instructions on how to use program:

```
python3 crypt.py -h
```

Create and store a new set of keys (both encrypt and decrypt)

```
python3 crypt.py -c <keyfilename>
```

Encrypt a given file:

```
python3 crypt.py -e <exiting keyfile name> <input filename> <output filename>
```

Decrypt a given file:

```
python3 crypt.py -d <exisiting keyfile name> <input filename> <output filename>
```

I've create starter code located in this folder (called crypt_starter.py).


