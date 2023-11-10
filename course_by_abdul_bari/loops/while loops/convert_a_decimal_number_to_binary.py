n = int(input("Enter a number: "))
bin = 0

while n > 0:
    r = n % 2 
    n = n // 2
    bin = bin * 10 + r   # the number will be in reserved from 

brev = 0

while bin > 0:
    r = bin % 10
    bin = bin // 10
    brev = brev * 10 + r  # it will reverse the number

print(brev)