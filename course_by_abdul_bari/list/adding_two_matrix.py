L1 = [[1,2,3,4], [1,2,3,4], [1,2,3,4]]
L2 = [[5,6,7,8], [5,6,7,8], [5,6,7,8]]

L3 = []

for i in range(3):
    sum = []
    for j in range(4):
        r = L1[i][j] + L2[i][j]
        sum.append(r)
    L3.append(sum)
print(L3)