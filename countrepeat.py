n = int(input())
lst1 = list(map(int,input().split()))[:n]
rep = []
for i in lst1:
    rep.append(lst1.count(i))
index = rep.index(max(rep))
print(lst1[index])
