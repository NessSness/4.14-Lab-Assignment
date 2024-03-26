# Name: Case Buckmaster
# Lab: 4.14
# Description: Takes a string as input, and returns a count of all characters
# except spaces, periods, or commas

# Variables

# Input for the string we will count later.
user_text = input()

# Used to count how many characters are in user_text.
char_count = 0

# Iterate through the string of user text.
for char in user_text:

    # Check if the current character is a space, period or comma. If not, add to the count.
    if (char != ",") and (char != " ") and (char != "."):
        char_count += 1

# Print the amount of characters counted in the string.
print(char_count)
