# 🚀 Project: Simple Budget Planner 💸
# 🧠 Objective:
# Build a simple console-based budget calculator that takes:
#
# Your monthly income
#
# Your expenses on rent, food, transport, and others
#
# Calculates:
#
# Total expenses
#
# Savings
#
# What percentage of your income you saved
#
# 🧾 Features You Must Use:
# ✅ Data types (integers, floats)
# ✅ Type checking/conversion (e.g., float(input(...)))
# ✅ PEMDAS for calculations
# ✅ round() for clean values
# ✅ Assignment operators like -= and /=
# ✅ Optionally: Use math.floor() to round down your savings


#Solution Below






















salary = float(input("What is your monthly salary?\n"))

rent = float(input("What is your rent? expenses\n"))

food_expense = float(input("What is your food? expenses\n"))

transport = float(input("What is your transport expenses?\n"))

others = float(input("What is your other expenses?\n"))


print(salary)
print(rent)
print(food_expense)
print(transport)
print(others)

print("-------Budget Summary-------")
total_expenses = (rent + food_expense + transport + others)
savings = (salary - total_expenses)
saved_income_percentage = ((savings/salary) * 100)

print(f"Your total expenses are: ${total_expenses}")
print(f"Savings you have made: ${savings}")
print(f"You have saved {saved_income_percentage}% of the salary")

print("----------------------------")
