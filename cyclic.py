n=int(input())
a=[]
for i in range (0,n):
    b=list(map(int,input().split()))
    a.append(b)
d=(a[0][1]-a[1][0])
print(d)