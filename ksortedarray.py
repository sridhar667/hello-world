k = int(input())
lst = []
for i in range(k):
    lst.append(list(map(int,input().split())))
ans = []
for i in lst:
    ans+=i
ans.sort()
print(*ans)
343