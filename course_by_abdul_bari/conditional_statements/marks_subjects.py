#check if a statement has passed or failed , by taking marks in 3 subjects .

math = int(input("Enter your math marks: "))
physics = int(input("Enter your physics marks: "))
chemistry = int(input("Enter your chemistry marks: "))

if math >= 45 and physics >= 45 and chemistry >= 45:
    print("passed ")
else:
    print("failed")
