n=int(input())
l=input().split(" ")
co=0
for i in range(len(l)):
    co=l.count(l[i])
    if co==1:
    	ans=l[i]
print(ans)