def total(*nums):
    print(type(nums))
    print(nums)
    sum = 0
    for elem in nums:
        sum = sum + elem
        print("sum =",sum)
    return sum

result = total()
print(result)