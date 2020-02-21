s,k=input().split()
lst1=list(s)
m=int(k)
lst=[]

for i in range(1,len(s)):
    if i==m-1:
        lst.append(s[i])
        for j in range(m,len(s)):
            a=i+m
            lst.append(s[a])
            break

print(' '.join(lst))
