n=input()
l=list(map(str,input().split()))
m=[]
for i in range (1,n):
 if l in m:
  m.pop(l)
 else:
     m.append(l)
print(m)