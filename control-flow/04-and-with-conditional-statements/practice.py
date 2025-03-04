age = int(input("Enter your age: "))
city = input("Enter your city: ")
if age>14 and age<=18 and city=="kabul":
    print("You are eligible for discount")
elif age>14 and age<=18 and city=="herat":
    print("You are eligible for discount")
else:
    print("You are not eligible for discount")
