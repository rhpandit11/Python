my_list = [1, 2, 3, 4, 5]

# Initialize two pointers: one at the beginning and one at the end of the list
start = 0
end = len(my_list) - 1

# Use a while loop to swap elements until the pointers meet in the middle
while start < end:
    # Swap elements at start and end indices
    my_list[start], my_list[end] = my_list[end], my_list[start]
    
    # Move the pointers towards the center of the list
    start += 1
    end -= 1

# Print the reversed list
print(my_list)