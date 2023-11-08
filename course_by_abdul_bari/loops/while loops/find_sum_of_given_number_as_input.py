num_of_numbers = int(input("Enter a number of numbers: ")) #Enter the number how many times you want to add the numbers
sum = 0
count = 0

while count < num_of_numbers:
    n = int(input("Enter a no: "))
    sum = sum + n
    count = count + 1
print("Sum of numbers are: ", sum)


