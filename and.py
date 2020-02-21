n=input()
k=list(map(int,input().split()))
c=0
for i in k:
    c=c&i
print(c)
