s,p =map(str,input().split(" "))
for i in range(len(s)):
    if s[i] in p:
        s[i].upper()
        
print(s,end=" ")
print(p)