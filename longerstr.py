s1,s2=map(str,input().split())
s1=list(s1)
s2=list(s2)
if len(s1)>len(s2):
    s=len(s1)-len(s2)
    for i in range(s):
        s1.pop()
else:
    s=len(s2)-len(s1)
    for i in range(s):
        s2.pop()
print(''.join(s1),end="")
print(''.join(s2))