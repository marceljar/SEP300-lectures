try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
except ValueError:
    print("That was not a valid number.")
else:
    try:
        print(f"{num}/{den} = {num/den}")
    except ZeroDivisionError:
        print("You cannot divide a value with zero")
    except:
        print("Something else went wrong")
