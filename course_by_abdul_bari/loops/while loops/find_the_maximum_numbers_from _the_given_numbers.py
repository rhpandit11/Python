num_of_numbers = int(input("Enter num_of_numbers: ")) # how many number of times you want to enter numbers
max = 0
count = 0

max =   int(input("Enter a number: ")) #if we are taking minus numbers as input

while count < num_of_numbers - 1:
    n = int(input("Enter a number: "))
    if n > max:        # if user have entered a number which is greater than max than take max = n
        max = n
    count = count + 1

print("Maximum Number is: ", max)