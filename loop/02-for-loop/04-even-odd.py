l = [1,2,3,4,5,6]
even_list = []
odd_list = []
for elem in l:
    if elem%2==0:
        even_list.append(elem)      
    else:
        odd_list.append(elem)
print("even list",even_list)
print("odd list",odd_list)