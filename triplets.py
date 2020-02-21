m=int(input())
x=list(map(int,input().split()))
t=0
y=list(set(x))
a=[]
for i in x:
  if i in y:
    a.append(i)
    y.remove(i)
n=len(a)
for i in range(n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
      if a[i]<a[j]and a[j]<a[k] and i<j and j<k:
        t+=1
if t!= 0:
    print(t)
else:
    print(-1)
