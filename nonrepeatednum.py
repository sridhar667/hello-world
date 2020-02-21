n=int(input())
l=input().split()
ans=l[0]
occ=0
for i in range(n):
  occ=l.count(l[i])
  if occ==1:
    ans=l[i]
print(ans)    