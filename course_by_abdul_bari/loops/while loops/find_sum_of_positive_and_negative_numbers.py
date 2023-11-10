num_of_numbers = int(input("Enter a num_of_numbers: "))
psum = 0 # positive sum 
nsum = 0 # Negative sum
count = 0 # for counting purpose

while count < num_of_numbers: # while loop should be work till the count is less than num_of_numbers
    n = int(input("Enter a number: "))
    if n > 0:    # if the number is greater than 0
        psum = psum + n   # do sum of positive number
    else:               #else if the number is less than 0 it is considered as negative
        nsum = nsum +n

    count = count + 1 # counting

print("Positive numbers sum ara: ",psum,"Negative numbers sum are: ",nsum)