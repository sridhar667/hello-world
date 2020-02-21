n = int(input())
lst = list(map(int,input().split()))
star = []
for i in range(n-1):
    m = max(lst[i+1:])
    star.append(m)
star.append(0)
print(*star)
