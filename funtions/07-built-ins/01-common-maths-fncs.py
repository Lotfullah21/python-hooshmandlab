a = int(input("a: "))
b = int(input("b: "))
def is_even(a, b):
    if a%b==0:
        return True
    return False
result = is_even(a,b)
print("result =",result)



def power(a, b):
    return a**b
result = power(a,b)




def divide(a, b):
    if b==0:
        return "You cannot enter zero for second parameter"
    return a/b


def multiply(a, b):
    return a*b


def subtract(a, b):
    return a-b

# # add
# def add(a,b):
#     return a + b

# total = add(a,b)
# print("total =",total)