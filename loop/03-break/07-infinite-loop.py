secret = "10"
for i in range(3):
    user_input = input("Enter your guess: ")
    if user_input ==secret:
        print("You are a winner!!!!")
        break
    else:
        print("Try again")