def first_digit(num):
    while num>=10:
        num = num//10
    print("first digit =", num)
num = int(input("Enter a number: "))
x = first_digit(num)
print(1)
