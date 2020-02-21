n=int(input())
li=list(map(int,input().split()))[:n]
li2=[]
tmp=[]
for i in range(n):
  tmp.append(li[i])
  li2.append(min(tmp))
print(*li2)