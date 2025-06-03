print("Check you password's strength by entering it here!")
entered_password = input("Enter you password: ")

length_of_password = len(entered_password)
uppercase = 0
lowercase = 0
digit = 0
special_char = 0
special_characters = "!@#$%^&*()-+?_=,<>/."

for char in entered_password:
    if char.isupper():
        uppercase += 1
    if char.islower():
        lowercase += 1
    if char.isdigit():
        digit += 1
    for n in special_characters:
        if char == n:
            special_char += 1
        else:
            special_char = 0


print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")
print(f"Digits: {digit}")
print(f"Special characters: {special_char}")
print(length_of_password)

print("Password check processing......")

if length_of_password < 6 and uppercase == 0 and lowercase == 0 and digit == 0 and special_char == 0:
    print("Weak 😩")
elif ((uppercase == 1 and lowercase == 1) or (lowercase == 1 and digit == 1) or
      (digit == 1 and special_char == 1) or (special_characters == 1 and uppercase == 1)):
    print("Moderate 😄")
elif length_of_password > 8 and uppercase and lowercase and digit and special_char:
    print("Strong 🔥")
else:
    print("404!")
