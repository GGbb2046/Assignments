# note: This is starter code for c05ex2

# define functions
import string
import random

def encrypt(encrypt_key, plaintext):
    ciphertext = ""
    for ch in plaintext:
        if ch in string.ascii_letters:
            ciphertext+=encrypt_key[ch]
        else:
            ciphertext+=ch
    return ciphertext

def decrypt(decrypt_key, ciphertext):
    plaintext = ""
    for ch in ciphertext:
        if ch in string.ascii_letters:
            plaintext+=decrypt_key[ch]
        else:
            plaintext+=ch
    return plaintext

def generate_keys():
    chars = string.ascii_letters
    codes = random.sample(chars,len(chars))
    decrypt_key = dict(zip(codes,chars))
    encrypt_key = dict(zip(chars,codes))
    return decrypt_key, encrypt_key

def print_instructions():
    print("This program encrypts and decrypts files using a word scramble cipher")
    print("  Usage:")
    print("    To get help:")
    print("         python crypt.py -h")
    print("    To create a key file:")
    print("         python crypt.py -c filename")
    print("    To encrypt a file:")
    print("         python crypt.py -e keyfile inputfile outputfile")
    print("    To decrypt a file:")
    print("         python crypt.py -d keyfile inputfile outputfile")
def print_error():
    print("ERROR: Invalid command line arguments!")

# main program

import sys


if len(sys.argv)==2 and sys.argv[1]=='-h': # if only two arguments this can only be help, so if we don't have -h then we have incorrect input
    print_instructions()
elif len(sys.argv)==3 and sys.argv[1]=='-c': # if there are 3 args, this can only be create new key file, if we don't have -c we have incorrect input
    ######################### INSERT CODE HERE ############################
    print("create keyfile") # replace this and insert create keyfile code here
elif len(sys.argv)==5 and sys.argv[1]=='-e': # if there are 3 args, this can only be create new key file, if we don't have -c we have incorrect input
    ######################### INSERT CODE HERE ############################
    print("Encrypt file") # replace this and insert encrypt file code here
elif len(sys.argv)==5 and sys.argv[1]=='-d': # if there are 3 args, this can only be create new key file, if we don't have -c we have incorrect input
    ######################### INSERT CODE HERE ############################
    print("Decrypt file") # replace this and insert decrypt file code here
else:
    print_error()
    print_instructions()
    



