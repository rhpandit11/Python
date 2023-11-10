n = int(input("Enter a number: ")) # taking input from user
sum = 0 # start sum value from 0
while n > 0: # while input number is greater than zero
    r = n % 10 # divide given number by 10
    n = n // 10 # divide it by 10 and make it into int using //
    sum = sum + r # modify counter value
print("Sum of digits are :",sum)
