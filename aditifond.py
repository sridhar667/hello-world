(s,h,d)=map(str,input().split())
s=list(s)
h=list(h)
d=list(d)
result=""
for i in s:
    if i in h:
        if i in d:
            result=result+i
if len(result)>0:
    print(result)
else:
    print("-1")