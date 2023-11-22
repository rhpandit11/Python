letter = input("enter the letter: ")
food = ['Pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']

for x in food:
    if x.startswith(letter):
        print(x)

