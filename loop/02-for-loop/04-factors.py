n = int(input("Enter a number: "))
factors = []
for elem in range(1,n+1):
    if n%elem==0:
        factors.append(elem)
print(factors)