num_of_numbers = int(input("Enter a num_of_numbers: "))
sum = 0
count = 0

while count < num_of_numbers:
    n = int(input("Enter a number: "))
    sum = sum + n
    count = count + 1

print(sum)