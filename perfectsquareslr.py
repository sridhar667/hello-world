import math

def isPerfect(n):
    s = math.sqrt(n)
    f = math.floor(s)
    return((s-f)==0)
    

x,y = map(int,input().split())
c=0
for i in range(x,y+1):
    if(isPerfect(i)):
        c+=1
print(c)
