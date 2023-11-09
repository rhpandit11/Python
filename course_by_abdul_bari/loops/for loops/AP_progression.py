a = int(input("Enter the first term: ")) 
d = int(input("Enter the common difference: "))
n = int(input("Enter the terms: "))

for t in range(a,a+n*d,d): #formula is a+n*d
    print(t)