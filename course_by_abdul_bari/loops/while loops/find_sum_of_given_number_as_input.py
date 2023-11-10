num_of_numbers = int(input("Enter a number of numbers: ")) #how many numbers you want to add together
sum = 0
count = 0   # for counting purpose

while count < num_of_numbers:  # while loop should be work till the count is less than num_of_numbers
    n = int(input("Enter a no: "))
    sum = sum + n
    count = count + 1   # add 1 in the present count
print("Sum of numbers are: ", sum)


