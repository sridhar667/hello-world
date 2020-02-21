l = input().split()
lst = []
for i in range(len(l)):
    if i%2==0:
        tmp=""
        lst=list(reversed(l[i]))
        tmp=tmp.join(lst)
        l[i]=tmp
print(" ".join(l))