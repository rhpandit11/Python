s1 = input("Enter a string")
s2 = input("Enter second string")

if len(s1) != len(s2):
    print('Not Anagram')
else:

    for x in s1:
        if x not in s2:
            print('Not Anagram')
            break
    else:
        print('Anagram')