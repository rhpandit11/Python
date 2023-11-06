#Total Surface area of a cuboid

length = float(input("Enter length"))
breadth = float(input("Enter breadth"))
height = float(input("Enter height"))

# font_and_back = 2(length*height)
# bottom_and_top = 2(length*breadth)
# left_and_right = 2(breadth*height)

total = 2 * (length * height + length * breadth + breadth * height)

print("Total surface area is", total)