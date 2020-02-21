n=int(input())
li=list(map(int,input().split()))[:n]
c=0
for i in range(n):
  for j in range(i+1,n-1):
    if li[i]+li[j] in li:
      c+=1
print(c)