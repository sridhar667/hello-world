s=input()
a=[]
w=[]
f=[]
for i in range(0,len(s)):
    if s[i].lower() in 'aeiou':
        a.append(s[i])
    else:
        w.append(s[i])
a.sort()
j=0
k=0
for i in range(0,len(s)):
    if s[i] in 'aeiou':
        f.append(a[j])
        j=j+1
    else:
        f.append(w[k])
        k=k+1
print(''.join(f))