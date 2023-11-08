num_of_numbers = int(input("Enter a number of numbers: ")) #how many numbers you want to add together
sum = 0
count = 0

while count < num_of_numbers:
    n = int(input("Enter a no: "))
    sum = sum + n
    count = count + 1
print("Sum of numbers are: ", sum)


