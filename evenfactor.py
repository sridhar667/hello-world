n = int(input())
lst = []
for i in range(1,n+1):
    if n%i==0:
        if i%2==0:  
            lst.append(i)
print(*lst)
98