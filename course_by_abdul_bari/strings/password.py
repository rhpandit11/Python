password1 = input("Enter your passowrd ")
password2 = input("confirm password")

if password1 == password2:
    print('password created')
else:
    if password1.casefold() == password2.casefold():
        print('Please check for the cases and try again')
    else:
        print("Try again")