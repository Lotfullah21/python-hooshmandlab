secret = "10"
while True:
    user_input = input("Enter your Guess: ")
    if user_input == secret:
        print("You are a winner!!!")
        break
    else:
        print("TRY AGAIN")