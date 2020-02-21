l,r,k = map(int,input().split())
c= 0
for i in range(l,r+1):
    if str(k) in str(i):
        c+=1
print(c)
301