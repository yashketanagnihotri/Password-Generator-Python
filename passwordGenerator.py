import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

noOfLetters = int(input("How many letters do you want in your password? : "))
noOfNumbers = int(input("How many numbers are needed? : "))
noOfSymbols = int(input("How many symbols are needed? : "))

password = ""

for i in range(noOfLetters):
    password += random.choice(letters)

for i in range(noOfNumbers):
    password += random.choice(numbers)

for i in range(noOfSymbols):
    password += random.choice(symbols)

# done for shuffling
finalPassword = list(password)
# this is how to convert string to a list
random.shuffle(finalPassword)
finalPassword = "".join(finalPassword)
print(f"Your password is : {finalPassword}")
