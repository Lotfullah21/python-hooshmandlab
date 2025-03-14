text = "Hello oo"
count = 0
for i in range(len(text)-1):
    if text[i]==text[i+1]:
        count = count +1
        print("character =",text[i])
print("count =",count)