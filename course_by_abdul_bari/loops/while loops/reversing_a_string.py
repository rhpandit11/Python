n = int(input("Enter a number: ")) # taking input from user
rev = 0 # starting reverse value from zero
while n > 0: # while input number is greater than zero
    r = n % 10 # divide given number by 10
    n = n // 10 # divide it by 10 and make it into integer using //
    rev = rev * 10 + r # modify counter value
print("Reverse of digits are :",rev)

print(n) # it will be zero because condition becomes false than loop exit and next statement is print
