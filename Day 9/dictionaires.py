# 🎯 Coding Challenge
# 🛍️ Shopping List Manager
# 👉 Create a dictionary called shopping_cart.
# Add 3 items and their prices.
# Then:
#
# Add a new item to the cart.
#
# Change the price of one existing item.
#
# Remove one item using .pop().
#
# Print the total cost of items left in the cart.
#
# 💡 Example Output:
# nginx
# Copy
# Edit
# Total cost: $26.5


shopping_cart = {
    "bread": 1,
    "chocolate": 5,
    "peanut_butter": 7,
}

shopping_cart["jam"] = 5
shopping_cart["chocolate"] = 2.7
shopping_cart.pop("bread")
print(shopping_cart)

total_bill = 0
for values in shopping_cart.values():
    total_bill += values

print(f"Total bill: ${total_bill}")


