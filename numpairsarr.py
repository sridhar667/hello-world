n=int(input())
li=list(map(int,input().split()))
c=0
for i in range(n):
  for j in range(i+1,n):
    if i<j and li[i]<li[j]:
      c+=1
print(c)