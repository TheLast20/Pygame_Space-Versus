L1 = [230, 32,56]
L2 = [324,12,56]
L3 = [324,12,56]
L4 = []
L5 = []

L3.sort()

for i in L3:
    L4.append(L1[L2.index(i)])
    L5.append(L2[L2.index(i)])

L1 = L4[::]
L2 = L5[::]
del L3
del L4
del L5

print(L1)
print(L2)
