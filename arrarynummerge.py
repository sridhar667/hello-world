k=int(input())
li=[]
for i in range(k):
  tmp=list(map(int,input().split()))
  li.extend(tmp)
li.sort()
print(*li)