n=input()
m=list(map(int,input().split()))
ans = []
for i in m:
    if m.count(i)==1:
        ans.append(i)
print(*ans)
    