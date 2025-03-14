text = "Hello world"
user_input = input("Enter your char: ").lower()
count = 0
for ch in text:
    if ch==user_input:
        count = count + 1
print(f"occurrence of char = {user_input} = {count}")


