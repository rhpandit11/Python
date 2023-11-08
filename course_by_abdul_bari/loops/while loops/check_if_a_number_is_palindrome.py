n = int(input("Enter a number: "))
m = n #storing the original value to n for further comparision
rev = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r
if m == rev: #comparing the number to check
        print("Number is a Palindrome")
else:
      print("Number is not a Palindrome")