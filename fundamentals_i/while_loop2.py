while True:
    user_input = input("Enter something (or 'q' to quit): ")
    if user_input.lower() == "q":
        print("Goodbye!")
        break
    else:
        print("You entered: ", user_input)