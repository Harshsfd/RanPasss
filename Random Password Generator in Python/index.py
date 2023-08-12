# Project Random Password Generator in Python
# Intern ID- CC51345
# Harsh Bhardwaj 
# Mail: harshbhardwaj1511@gmail.com 
# Designation- Python Development Intern
# Batch- August 2023
import random

# Define the character set that you want to use for your password.
# This could include letters, numbers, and symbols.
character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=+{}[]<>,./?"

# Generate a random password of the desired length.
password_length = 8
password = ""
for i in range(password_length):
    # Choose a random character from the character set.
    rand_char = random.choice(character_set)

    # Add the character to the password.
    password += rand_char

# Print the password to the console.
print(password)