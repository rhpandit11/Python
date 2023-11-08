n = int(input("Enter a number: "))
m = n
rev = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r
if m == rev:
        print("Palindrome")
else:
      print("Not Palindrome")