#FOR LOOP


# fruits = ['apple', 'pear', 'banana', 'mango']
# for fruit in fruits:
#     print(fruit)
#     print(fruit+ " pie")
# score = 87, 42, 99, 23, 54, 67, 88, 91, 50, 78, 96, 64, 30, 83, 47, 75, 66, 49, 68, 90, 80, 71, 84, 45, 77
# jumlah=sum(score)
# print (f"jumlah score : {jumlah}")
# tertinggi=max(score)
# print (f"score tertinggi: {tertinggi}")
# total = 0
# for angka in range(1, 101):
#     total += angka
# print(total)

# for number in range(1, 101):
#     if number %3 == 0 and number %5 == 0:
#         print('FizzBuzz')
#     elif number %3 == 0:
#         print('Fizz')
#     elif number %5 == 0:
#         print('Buzz')
#     else:
#         print(number)

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = [] #untuk menyimpan password
for char in range(0, nr_letters):
    password_list.append(random.choice(letters)) #untuk menambahkan huruf random

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols)) #untuk menambahkan simbol random

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers)) #untuk menambahkan angka random

print(password_list)
random.shuffle(password_list) #untuk mengacak password
print(password_list)

password = ""
for char in password_list: #untuk mengambil karakter tanpa list
    password += char 

print(f"Your password is: {password}")






