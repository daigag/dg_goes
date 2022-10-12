monthly_salary = float(input("What is your montly salary? "))
service_years = float(input("How many years have you worked here? "))

bonus = monthly_salary * 0.15 * service_years

if service_years < 2:
    print("Your bonus amount is 0! Keep trying!")
else:
    print(f'Your bonus amount is {bonus}')
    
