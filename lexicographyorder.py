n=int(input())
l=[x for x in input().split()]
l2=sorted(l)
l3=sorted(l2,key=len)
print(*l3,end="")