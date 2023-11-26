name = input("Enter a name: ")

birthdays = {
    'sachin' : '03/14/2003',
    'Rahul'  : '11/02/2000'
    }

if name in birthdays:
    print(name,birthdays[name])
else:
    print("Name is not found")