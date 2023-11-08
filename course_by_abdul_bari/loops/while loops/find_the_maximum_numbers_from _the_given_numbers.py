num_of_numbers = int(input("Enter num_of_numbers: "))
max = 0
count = 0

max =   int(input("Enter a number: ")) #if we are taking minus numbers as input

while count < num_of_numbers - 1:
    n = int(input("Enter a number: "))
    if n > max:
        max = n
    count = count + 1

print("Maximum Number is: ", max)