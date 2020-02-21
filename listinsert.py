import bisect
li=[2,3,5,]
li1=[]
x=int(input())
pos=bisect.bisect(li,x)
j=0
for i in range(0,len(li)+1):
    if (i!=pos):
        li1.append(li[j])
        j=j+1
    else:
        li1.append(x)
print(li1)