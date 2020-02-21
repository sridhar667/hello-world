from collections import Counter
n=int(input())
li=list(map(int,input().split()))[:n]
c=Counter(li)
for e,co in c.items():
  if co==1:
    print(e)
    break