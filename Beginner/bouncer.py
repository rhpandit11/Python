age = input("How old are you: ")
if age != "":
    age = int(age)
    if age >= 18 and age < 21:
        #18-21 wristband
        print("you can enter, but need a wristband")
    elif age >= 21:
        print("You are good to enter and can drink!")
    else:
        #too young. sorry
        print("You can't come in, little one! :(")
else:
    print("please enter  an age!")