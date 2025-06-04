# 🎯 Project Goal
# Build a Caesar Cipher Encoder and Decoder
# It should take a message and shift each letter by a certain number of places in the alphabet.
#
# Example:
#
# Original: hello
#
# Shift: 3
#
# Encrypted: khoor
#
# 📋 Instructions
# The user will choose whether they want to encode or decode a message.
#
# The user enters the message.
#
# The user enters a shift number (1–25).
#
# The function will shift each letter by that amount in the alphabet.
#
# Display the final encoded or decoded message.
#
# The program should run in a loop until the user decides to quit.
#
# 💡 Hints
# Use a list of letters:
#
# python
# Copy
# Edit
# alphabet = ['a', 'b', 'c', ..., 'z'] * 2
# Duplicating the list helps with easy wrap-around.
#
# Convert user input to lowercase using:
#
# python
# Copy
# Edit
# message.lower()
# Make sure you preserve non-alphabet characters (like spaces, punctuation).
#
# Make sure the shift works in both directions:
#
# Encoding → shift forward
#
# Decoding → shift backward
#
# Use a loop to allow repeated use.
# Instructions and Hints ☝️⬆️

logo = """
   _____                       _____  _                 
  / ____|                     / ____|| |                
 | |      ___   ___  _ __    | |     | |__    ___  _ __ 
 | |     / _ \ / _ \| '_ \   | |     | '_ \  / _ \| '__|
 | |____| (_) | (_) | |_) |  | |____ | | | ||  __/| |   
  \_____|\___/ \___/| .__/    \_____||_| |_| \___||_|   
                    | |                                
                    |_|   by Day 8 - Python Learners
"""
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z'] * 2

print(logo)

is_quit = False

def encode(message, shift_number):
    encoded_message = ''
    for letter in message:
        if letter.isalpha():
            aplhabet_char_index = alphabets.index(letter)
            shifted_letter_index = aplhabet_char_index + shift_number
            shifted_characters = alphabets[shifted_letter_index]
            encoded_message += shifted_characters
        else:
            encoded_message += letter

    print(encoded_message)



def decode(message, shift_number):
    decoded_message = ''
    for letter in message:
        if letter.isalpha():
            aplhabet_char_index = alphabets.index(letter)
            shifted_letter_index = aplhabet_char_index - shift_number
            shifted_characters = alphabets[shifted_letter_index]
            decoded_message += shifted_characters
        else:
            decoded_message += letter

    print(decoded_message)



while not is_quit:
    users_choice = input("Write 'encode' to encrypt a message, or 'decode' to decrypt the message: ").lower()
    if users_choice == "encode":
        encode(message=input("Type the message: ").lower(), shift_number=int(input("Enter the shift number: ")))
    elif users_choice == "decode":
        decode(message=input("Type the message: ").lower(), shift_number = int(input("Enter the shift number: ")))
    else:
        print("Error ❌, Please only choose encode or decode, Try Again!")

    wanna_quit = input("If you want to quit here then type 'yes ✅', otherwise type 'no ❌' to continue: ").lower()
    if wanna_quit == "yes":
        is_quit = True
        print("This is it, Thanks for using our program.")

    elif wanna_quit == "no":
        is_quit = False
    else:
        print("You made a type, Try Again ❌")

