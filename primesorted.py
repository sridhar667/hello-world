n = int(input())
lst = []
if n%2==0:
    lst.append(2)
for i in range(3,n+1):
    if n%i==0:
        if i%2!=0:
            lst.append(i)
lst.sort()
for i in lst:
    l=2
    while(l<i):
        if i%l==0:
            lst.remove(i)
            break
        l+=1
lst = map(str,lst)
print(' '.join(lst))
