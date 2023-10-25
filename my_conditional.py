enter = str(input("Do You wont get monny?: "))
if enter == "yes":

    sec_enter = int(input("Enter amount geting mony: "))
    balans = 10000
    rest = int(sec_enter - balans)
    # if enter == str("Yes"):

    if sec_enter <= 0 or sec_enter >= 10000:
        print("it is not posable!!!")
    else:
        print("You are welcom, get Your monyy")
        
        print("Your rest balanse", rest)
else:
    print("Thank You and Gudbay")
