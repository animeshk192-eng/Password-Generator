
print("Welcome to Password Genrator")

import random

letters = ("abcdefghijklmnopqrstuvwxyzABCDEFGJIKLMNOPQRSTUVWXYZ")

numbers = "0123456789"

symbols = "!@#$%^&*"

characters = letters + numbers +symbols

lenght = int(input("Enter password lenght: "))

passwrod = ""

for i in range(lenght):
    passwrod += random.choice(characters)


print("Generated Password:", passwrod)
