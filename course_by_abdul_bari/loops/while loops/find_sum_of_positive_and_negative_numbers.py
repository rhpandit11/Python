num_of_numbers = int(input("Enter a num_of_numbers: "))
psum = 0
nsum = 0
count = 0

while count < num_of_numbers:
    n = int(input("Enter a number: "))
    if n > 0:
        psum = psum + n
    else:
        nsum = nsum +n

    count = count + 1

print("Positive numbers sum ara: ",psum,"Negative numbers sum are: ",nsum)