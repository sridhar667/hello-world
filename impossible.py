from itertools import permutations
s = input()
L = [ ''.join(x) for x in list(permutations(s,len(s)))]
L2 = list(set(L))
L2.sort()
d=0
for i in L2:
    if int(i)>int(s):
        d=i
        break
if d:
    print(d)
else:
    print("impossible")