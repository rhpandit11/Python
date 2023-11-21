# L1 = [12,48,55,12,55]
# L2 = []
# [L2.append(x) for x in L1 if x not in L2]
# print(L2)

L1 = [3,5,7,9,3,6,5,2,3,7,10]

L2 = []

for x in L1:
    if x not in L2:
        L2.append(x)
print(L2)


# printing list without creating new list

L1 = [3,5,7,9,3,6,5,2,3,7,10]

# index = 0

# while index < len(L1):
#     current_element = L1[index]
#     if L1.count(current_element) > 1:
#         L1.remove(current_element)
#     else:
#         index += 1

# print(L1)