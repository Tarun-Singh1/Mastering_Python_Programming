# 🧩 Challenge: Scholarship Eligibility Checker
# 🔨 Your Task:
# Write a program that checks if a student is eligible for a scholarship.
#
# Ask for:
#
# GPA (on a 4.0 scale)
#
# Number of community service hours
#
# If the GPA is 3.5 or higher and they have at least 30 hours of service:
#
# Print "You are eligible for the scholarship!"
#
# Otherwise:
#
# Print "You do not meet the requirements."
#


#---------------Solution Below -----------------#





















print("Let's checks if yoou are eligible for a scholarship or not.")

gpa = float(input("Enter your weighted GPA (on a 4.0 scale): "))
service_hours = int(input("Enter your number of community service hours: "))

if gpa >= 3.5 and service_hours >= 30:
    print("You are eligible for the scholarship!")
else:
    print("You do not meet the requirements.")