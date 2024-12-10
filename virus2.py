print("virus activated!")
deactivate = input("do you want to de-activate virus? (yes/no) ")
while True:
    if deactivate == "no":
        print("You have a virus")
    elif deactivate == "yes":
        print("You have a virus")
    else:
        print("You didn't enter yes or no")
        deactivate = input("do you want to de-activate virus? (yes/no) ")
