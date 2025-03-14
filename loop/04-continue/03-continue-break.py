x = [1,12,30,40,111,50,100,3,11]
for ele in x:
    if ele%5==0:
        continue
    if ele%6==0: 
        break
    print(ele)