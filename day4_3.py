# 3. Primes Check if entered positive number is a prime number.

#  A prime number is a number that divides without remainder only by itself and 1.

number = int(input("Please enter a positive number to check if it is prime "))

if number % 2 == 0:
    print(f"Sorry {number} is not a prime number because it divides by 2")
elif number % 3 == 0:
    print(f"Sorry {number} is not a prime number because it divides by 3")
elif number % 5 == 0:
    print(f"Sorry {number} is not a prime number because it divides by 5")
elif number % 7 == 0:
    print(f"Sorry {number} is not a prime number because it divides by 7")
else:
    print(f'{number} is prime number!')