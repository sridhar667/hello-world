n,k = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
L2 = []
for x in L :
    L2.append((x,abs(x-k)))
L2.sort(key=lambda x : x[1])
L3 = []
for i in range(1,4) :
    L3.append(L2[i][0])
print(*L3,end='')