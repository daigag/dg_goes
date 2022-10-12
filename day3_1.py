temperature = float(input("What is your temperature? "))

if temperature < 35:
    print("not too cold")
elif temperature > 35 and temperature <= 37:
    print("all right")
else:
    print('possible fever')
