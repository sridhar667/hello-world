def gcd(a,b):
    if a==0:
        return b
    else:
        rem = b%a
        return(gcd(rem,a))
        
n = int(input())
lst = list(map(int,input().split()))[:n]
res = gcd(lst[0],lst[1])
for i in range(2,len(lst)):
    res = gcd(res,lst[i])
print(res)
