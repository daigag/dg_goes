
# Ask user to enter the height of the tree 

# Then Print the tree: Ex. height == 3 

# The printout would be: 

#   * 

#  *** 

# ***** 

# Note: remember that several symbols can be 
# printed at once, for example: print ("" * 10 + "*" * 6)




heigh = int(input("Please enter height of the tree: "))

for i in range(1, heigh+1):
    print(" "* int(heigh-i/2) + "*" * i)

