#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwd_len = nr_letters + nr_numbers + nr_symbols

all_char = []

for i in range(0, nr_letters):
  all_char.append(random.choice(letters))

for i in range(0, nr_symbols):
  all_char.append(random.choice(symbols))

for i in range(0, nr_numbers):
  all_char.append(random.choice(numbers))

your_pwd = ""
for i in range (0, pwd_len):
  pwd_char = random.choice(all_char)
  your_pwd += pwd_char 

print(f"Your Password is {your_pwd}")
