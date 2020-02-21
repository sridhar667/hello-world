n = int(input())
lst = list(map(int,input().split()))
ans = []
for i in lst:
    if i not in ans:
        ans.append(i)
    else:
        ans.remove(i)
print(*ans)
242