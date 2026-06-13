import random
import string

print("===== Password Generator =====")

length = int(input("Enter password length: "))

include_numbers = input("Include numbers? (yes/no): ").lower()
include_symbols = input("Include symbols? (yes/no): ").lower()

characters = string.ascii_letters

if include_numbers == "yes":
    characters += string.digits

if include_symbols == "yes":
    characters += string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)