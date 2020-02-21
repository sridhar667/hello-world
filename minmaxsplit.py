n,k=map(int,input().split())
a=list(map(int,input().split()))
max=a[0]
for i in range(1,n):
  if a[i]>max:
    max=a[i]
x=a[1]
y=a[-1]
import random
print(random.choice([x,y]))