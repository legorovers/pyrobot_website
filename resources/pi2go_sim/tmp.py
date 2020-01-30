while True:
    number = input("Please enter a number\n")

    try:
        new_number = int(number) * 10
        print(new_number)
        break
    
    except:
        print("That was not a number.  Please try again")
