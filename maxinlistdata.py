n,k=map(int,input().split())
m=list(map(int,input().split()))
l=list(map(int,input().split()))
lst=[]
for i in range(k):
    m.append(i)
    lst.append(max(m))
print(*lst)