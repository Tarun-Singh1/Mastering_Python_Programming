# 🛠 Challenge Time!
# 📚 School Report Builder
# Create a list called report with 3 dictionaries.
# Each dictionary should contain:
#
# "name" (str)
#
# "marks" (a list of 3 integers)
#
# Your tasks:
#
# Add a new student to the list.
#
# Print each student’s name and average marks.
#
# Print the name of the student with the highest average.
#
# 💡 Expected Output:
# nginx
# Copy
# Edit
# Riya has an average of 84.67
# Aman has an average of 78.33
# Simran has an average of 91.0
# Simran has the highest average score.


report = [
    {"student": "Aman", "marks": [73, 79, 71]},
    {"student": "Riya", "marks": [83, 88, 91]},
    {"student": "Simran", "marks": [99, 96, 94]},
]

report.append({"student": "Shreya", "marks": [91, 89, 78]})

highest_score = 0
top_student = ''
for student in report:
    average_marks = (sum(student["marks"]) / len(student["marks"])).__round__(2)
    print(f"{student["student"]} has an average of {average_marks}")

    if average_marks > highest_score:
        highest_score = average_marks
        top_student = student["student"]

print(f"{top_student} has the highest average score {highest_score}")



