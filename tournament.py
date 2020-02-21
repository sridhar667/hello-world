n = int(input())
s = 2
while(1):
    if s<=n:
        s = s*2
    else:
        s = s//2
        break
print(n-s)
