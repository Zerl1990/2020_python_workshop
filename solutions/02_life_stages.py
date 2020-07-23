current_year = int(input("Please provide the current year:"))
birth_year = int(input("Please provide birth year:"))
age = current_year - birth_year
print(f"Your age is {age}")

if age <= 11:
    print('Your a child')
elif 11 < age <= 20:
    print('Your are a teenager')
elif 20 < age <= 35:
    print("You are a young adult")
else:
    print("You are adult")
