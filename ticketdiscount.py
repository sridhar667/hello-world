n=int(input())
l=list(map(int,input().split()))
m=int(input())
res=[]
for i in l:
    if i%m==0:
      res.append('1')
    else:
      res.append('0')
print(*res)