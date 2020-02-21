m,n = map(int,input().split())
lst = []
for i in range(m,n+1):
    if i%2!=0:
        lst.append(i)
print(sum(lst))
