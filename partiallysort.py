n=int(input())
a= list(map(int,input().split()))
x,y = map(int,input().split())
for i in range(x,y):
  for j in range(i,y+1):
    if a[i]<a[j]:
      a[i],a[j] = a[j],a[i]
b=[]
for i in a:
  b.append(i)
print(*b)