n = int(input("Enter a number: ")) # taking input from user
m = n #storing the original value to n for further comparision
rev = 0 # starting value zero 

while n > 0: # while input number is greater than zero
    r = n % 10 # divide given number by 10
    n = n // 10 # divide it by 10 and make it into int using //
    rev = rev * 10 + r # modify counter value
if m == rev: # if value of m is equal to rev then print if block 
        print("Number is a Palindrome")
else:  # else if value is not equal print else block                         
      print("Number is not a Palindrome")