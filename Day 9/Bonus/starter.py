# 🎯 Project Goal
# Create a Python program that simulates a Magic 8 Ball toy. The program should:
#
# Prompt the user to ask a yes/no question.
#
# Randomly select and display a response from a predefined set of answers.
#
# Continue this interaction until the user decides to quit.
#
# 🛠️ Instructions
# Import the Necessary Module
#
# Use Python's random module to facilitate random selection of responses.
#
# Define Possible Responses
#
# Create a collection (e.g., a list or dictionary) containing various Magic 8 Ball responses.
#
# These can include affirmative, non-committal, and negative answers.
#
# Implement User Interaction Loop
#
# Use a loop to continuously prompt the user for a question.
#
# Allow the user to exit the program by typing a specific command (e.g., 'exit' or pressing Enter).
# geeksforgeeks.org
#
# Generate and Display Random Response
#
# Upon receiving a question, randomly select a response from your predefined collection.
#
# Display the selected response to the user.
#
# Enhance User Experience
#
# Add introductory messages to welcome the user.
#
# Provide clear instructions on how to use the program and how to exit.
#
# 💡 Hints
# Using Dictionaries: While a list is commonly used for storing responses, you can utilize a dictionary to categorize
# responses (e.g., positive, neutral, negative) and randomly select a response from a specific category if desired.
#
# Random Selection: The random.choice() function is useful for selecting a random item from a list. If using a dictionary,
# you might first select a random key (category) and then a random response within that category.
#
# Input Handling: Use the input() function to capture user questions. Remember to handle cases where the user wants
# to exit the program.
#
# Loop Control: A while loop is effective for continuously prompting the user until they choose to exit.
#
# User Feedback: Providing feedback messages enhances user engagement. For example, acknowledging the users question
# before displaying the Magic 8 Bells response.

# Hints ⬆️

# Dictionary mapping numbers to Magic 8 Ball responses
responses = {
    1: "It is certain.",
    2: "It is decidedly so.",
    3: "Without a doubt.",
    4: "Yes – definitely.",
    5: "You may rely on it.",
    6: "As I see it, yes.",
    7: "Most likely.",
    8: "Outlook good.",
    9: "Yes.",
    10: "Signs point to yes.",
    11: "Reply hazy, try again.",
    12: "Ask again later.",
    13: "Better not tell you now.",
    14: "Cannot predict now.",
    15: "Concentrate and ask again.",
    16: "Don't count on it.",
    17: "My reply is no.",
    18: "My sources say no.",
    19: "Outlook not so good.",
    20: "Very doubtful."
}
