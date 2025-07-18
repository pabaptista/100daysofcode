#!/usr/bin/env python3

import random

def generate_password(numberOfLetters: int, numberofSymbols: int, numberOfNumbers: int) -> str:
    password = ""
    lettersUsed = 0
    numbersUsed = 0
    symbolsUsed = 0

    passwordSize = numberOfLetters + numberofSymbols + numberOfNumbers

    optionsAvailable = ["number", "letter", "symbol"]

    letters = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "w", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "W", "Z"]
    numbers = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = [ "!", "#", "$", "%", "&", "(", ")", "*", "+" ]

    while(len(password) < passwordSize):
        option = optionsAvailable[random.randint(0, 2)]
        if(option == 'number' and numbersUsed < numberOfNumbers):
            #password += numbers[random.randint(0, len(numbers)-1)]
            password += random.choice(numbers)
            numbersUsed+=1
        elif(option == 'letter' and lettersUsed < numberOfLetters):
            #password += letters[random.randint(0, len(letters)-1)]
            password += random.choice(letters)
            lettersUsed+=1
        elif(option == 'symbol' and symbolsUsed < numberofSymbols):
            #password += symbols[random.randint(0, len(symbols)-1)]
            password += random.choice(symbols)
            symbolsUsed+=1

    return password


print("Welcome to the password generator!")

letters = int(input("How many letters do you want in your password?\n"))
symbols = int(input("How many symbols do you want in your password?\n"))
numbers = int(input("How many numbers do you want in your password?\n"))

password = generate_password(numberOfLetters=letters, numberofSymbols=symbols, numberOfNumbers=numbers)

print(password)