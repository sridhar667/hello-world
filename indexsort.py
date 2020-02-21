n=input()
m=list(map(int,input().split()))
ans = []
count = 0
for i in m:
    if i==count:
        ans.append(i)
    count+=1
print(*ans)