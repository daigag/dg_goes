# # 1. FizzBuzz 

# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 36, .... to 97, Buzz, 99, Fizz 

# So if number divided by 5 then Fizz If divided by 7 then Buzz,
#  If divided by 5 AND 7 then FizzBuzz otherwise the same number

for i in range(1,100):
    if i%5==0:
        print("Fizz", end=", ")
    elif i%7==0:
        print("Buzz", end=", ")
    elif i%5==0 and i%7==0:
        print("FizzBuzz", end=", ")
    else:
        print(i, end=", ")
