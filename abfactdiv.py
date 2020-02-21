n,k=map(int,input().split())
fact=1
for i in range(1,n+1):
    a=fact*i
    b=fact*i
    c=a/b
    print(c)