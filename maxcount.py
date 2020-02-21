n= int(input())
a= list(map(int,input().split()))
max=0
t=1
for i in range(n-1):
  if a[i] < a[i+1] :
    t+=1
    #print(a[i],a[i+1],t)
  else:
    if t> max:
      max= t
    t=1
    #print(a[i],a[i+1],t)
if t> max:
  max=t
print(max)
