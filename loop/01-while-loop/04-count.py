x = int(input("Enter a number: "))
x = abs(x)
count = 0
while x>0:
    count = count + 1
    x = x//10
print("Count =",count)