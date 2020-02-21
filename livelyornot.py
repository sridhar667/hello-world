s=input()
l=[]
for i in s:
    l.append(s.count(i))
if len(set(l))==1:
    print(1)
else:
    print(0)
    
