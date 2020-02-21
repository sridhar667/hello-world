import math
n,k=map(int,input().split())
m=list(map(int,input().split()))
if k in m:
    s=m.index(k)
    if  k==s:
        print(-1)
    else:
        print(s)    
else:
    lst=[]
    for i in m:
        h=k-i
        lst.append(abs(h))
    d=min(lst)
    d=lst.index(d)
    print(m[d])