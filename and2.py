n=input()
k=list(map(int,input().split()))
for i in range(0,len(k)-1):
    c=k[i]&k[i+1]
print(c)
