n=int(input())
li=list(map(int,input().split()))[:n]
m=int(input())
li1=list(map(int,input().split()))[:m]
li.extend(li1)
st=set(li)
li=list(st)
li.sort()
print(*li)