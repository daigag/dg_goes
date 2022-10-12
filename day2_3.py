
precision = 4
t = float(input("What is the temperature in Celsius?\n")) 
t_fahrenheit = 32 + t * (9 / 5)
print(f"Current temperature in Celsius is: {round(t, precision)}")
print(f"Current temperature in Fahrenheit is: {round(t_fahrenheit, precision)}") 