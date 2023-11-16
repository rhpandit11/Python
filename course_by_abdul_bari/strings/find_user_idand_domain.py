email = input("Enter your mail")

userId = email.find('@')
print(userId)

print('user id:', email[:userId])
print('domain name:', email[userId+1:])