Students = {}

for i in range(1):
    name = input('Enter name: ')
    roll = int(input("Enter Roll: "))
    dept = input('Enter dept: ')
    Students[name] = {'Roll':roll,  'Name':name, 'Dept':dept}

print(Students)