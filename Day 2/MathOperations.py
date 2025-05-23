# 🧩 Coding Challenge: PEMDAS
# 🎯 Problem:
# Write a program to evaluate the final price of a product with:
#
# base_price = 100
#
# tax_rate = 18 (in percentage)
#
# discount = 5 (in percentage)
#
# Steps:
#
# Add tax to the base price.
#
# Subtract the discount from the result.
#
# Print the final price (rounded to 2 decimal places).


base_price = 100
tax_rate = 18
discount = 5

final_price = ((base_price + (base_price * tax_rate/100)) - base_price * discount/100)
print(f"Your final bill is: {final_price}")












