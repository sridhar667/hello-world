n=input()
m=input()
r,k=map(str,input().split(" "))
l=[]
l1=[]
for i in n:
    l.append(i)
for i in m:
    l1.append(i)
n=0
m=0
for i in range(l.index(r)+1,l.index(k)):
    n+=1
for i in range(l1.index(r)+1,l1.index(k)):
    m+=1
if(n < m):
    print(n)
else:
    print(m)