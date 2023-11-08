num_of_numbers = int(input("Enter num_of_numbers: "))
max = 0
count = 0

while count < num_of_numbers:
    n = int(input("Enter a number: "))
    if n > max:
        max = n
    count = count + 1

print("Maximum Number is: ", max)