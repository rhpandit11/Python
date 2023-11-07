year = int(input("Enter the Year: "))

if year % 100 == 0 :
    if year % 400 == 0 :
        print("Leap Year")
    else:
        print("Not a leap year")
elif year % 4 == 0 :
    print("Leap Year")
else:
    print("Not a Leap Year")


# year = int(input("Enter the Year: "))

# if year % 400 == 0 and year % 100 == 0 :
#     print("Leap Year")
# if year % 4 == 0 and year % 100 != 0 :
#    print("Leap Year")
# else:
#     print("Not a Leap Year")
