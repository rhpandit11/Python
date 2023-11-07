#Check if a person is authorise for admin access

username = input("Enter your name: ")

if username == 'john' or username == 'smith':
    print("Authorised")
else:
    print("Not Authorised")