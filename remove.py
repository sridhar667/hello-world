s=list(input())
i=0
while True:
    if i>=len(s)-1:
        break
    if s[i]==s[i+1]:
        x=s[i]
        s.remove(x)
        s.remove(x)
        i=0
    else:
        i=i+1
print(''.join(s) if len(s) else "-1")

