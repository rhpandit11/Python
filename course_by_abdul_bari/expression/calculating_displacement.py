#Calculating Displacement

u = float(input("Enter final_velocity "))
v = float(input("Enter final_initial_velocity "))
a = float(input("Enter acceleartion "))

displacement = (v**2 - u**2) / (2 * a)

print("displacement is ", displacement)