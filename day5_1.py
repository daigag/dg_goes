# Write a program for text conversion
# Save user input
# Print the entered text without changes

# Exception: if the words in the input are not .... bad, 
# then the output is not ...  bad section must be changed to is good



# Examples:

# The weather is not bad -> The weather is good

# The car is not new -> The car is not new

# This cottage cheese is not so bad -> This cottage cheese is good 



text = input("Enter Your text, tell me about today's weather?")

x = text.replace("not bad", "good")

print(x)

