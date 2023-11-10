n = int(input("Enter a number: ")) # taking input from user 
count = 0 # counter starting from 0
while n > 0: # while input number is greater than zero  
    n = n // 10 # divide it by 10 and make it into int using // floor division
    count = count + 1 # modify counter value
print("Number of digits are :",count) # print the output
