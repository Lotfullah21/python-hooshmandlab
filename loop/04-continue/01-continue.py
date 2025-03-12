l = [1,2,3,4,5,6,7,9,0]
for ele in l:
    if ele%5==0:
        print("Target found",ele)
        continue
    else:
        print(ele)
print("Target not found")
