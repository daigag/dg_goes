# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: Let the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). year

import datetime

username = input("What is your name?")
print(f"{username}, how old are you?")
age = int(input())
current_year = datetime.datetime.now().year
target_age = 100 - age
target_year = current_year + target_age
print(f'Nice! In {target_year} you will be 100 year old!')
