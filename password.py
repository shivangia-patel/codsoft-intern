#random password
import random
import string

length = int(input("enter length:"))

chars = string.ascii_letters
chars += string.digits
chars +=string.punctuation

password = ""

for i in range(length):
    next_character = random.choice(chars)
    password += next_character
    
print("your random password is:" ,password)