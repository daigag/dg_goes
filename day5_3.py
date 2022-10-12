# # 1. Confusion

# # The user enters a name.

# # You print user name in reverse (should begin with capital letter)
# #  then extra text: ",a thorough mess is it not ", then the first name of the user name then "?"

name = input("Please enter your name: ")

reversed = name[::-1].capitalize()

print(f'{reversed}, a thorough mess is it not, {name[0]}?')

