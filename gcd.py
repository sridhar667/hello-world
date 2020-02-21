def gcd(a,b):
    if a==0:
        return b
    else:
        rem = b%a
        return(gcd(rem,a))
        
n,q= map(int,input().split())
lst = list(map(int,input().split()))[:n]
a,b=map(int,input().split())
print()
