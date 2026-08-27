age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to vote.")
    citizenship = input("Are you a Canadian citizen? (T/F)")
    if citizenship == "T":
        print("You are eligible to vote.")
    else:
        print("You must be a citizen to vote.")    
else:
    print("Sorry, you are not old enough to vote.")