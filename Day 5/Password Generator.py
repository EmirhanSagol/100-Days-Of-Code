import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
unordered_password = []
password = ""

print("Welcome to the PyPassword Generator!")
in_letters = int(input("How many letters would you like in your password?\n"))
in_symbols = int(input("How many symbols would you like?\n"))
in_numbers = int(input("How many numbers would you like?\n"))

for letter in range(0, in_letters):
    unordered_password.append(random.choice(letters))

for symbol in range(0, in_symbols):
    unordered_password.append(random.choice(symbols))

for number in range(0, in_numbers):
    unordered_password.append(random.choice(numbers))
print(unordered_password)
random.shuffle(unordered_password)

for char in unordered_password:
    password += char

print(password)

