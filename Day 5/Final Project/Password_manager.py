import itertools
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))




















# for number in range(1, nr_numbers + 1):
#     random_num_list = random.sample(numbers, number)
#
# for letter in range(1, nr_letters + 1):
#     randon_letter_list = random.sample(letters, letter)
#
# for symbol in range(1, nr_symbols + 1):
#     random_symbol_list = random.sample(symbols, symbol)
#
#
# total_char = nr_symbols + nr_letters + nr_numbers
#
# sequenced_list = [x for x in itertools.chain (randon_letter_list, random_num_list, random_symbol_list)]
#
# # print(sequenced_list)
#
# random.shuffle(sequenced_list)
# # print((sequenced_list))
#
# final_password = ""
# for char in sequenced_list:
#     final_password += char
#
# print(f"You strong password is generated: {final_password}")






