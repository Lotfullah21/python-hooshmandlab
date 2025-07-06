def fact(num):
    if num==0:
        return 1
    ans = 1
    for ele in range(1, num+1):
        ans = ans * ele
    return ans
x = int(input("Enter a number: "))
factorial = fact(x)
print("factorial of",x,"=", factorial)
