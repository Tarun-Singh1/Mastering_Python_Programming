# 🧩 Coding Challenge: Number Manipulation
# 🎯 Problem:
# You are given:
#
# product_price = 345.678
#
# You need to:
#
# Round it to 1 decimal place.
#
# Floor it to the nearest whole number.
#
# Apply a 15% discount using -= shorthand.
#
# Print all the results.
#

import math

product_price = 345.678

rounded_price = round(product_price, 1)           # 345.7
print("Rounded Price:", rounded_price)

floored_price = math.floor(product_price)         # 345
print("Floored Price:", floored_price)

discounted_price = rounded_price                  # work with the accurate value
discounted_price -= discounted_price * 0.15       # apply 15% discount
print("Price after 15% discount:", round(discounted_price, 2))  # 293.85




















