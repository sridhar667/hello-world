s1= input()
s2=input()
if len(s1)>len(s2):
    b = s1.find(s2)
    if b!=-1:
        print(b)
else:
    b = s2.find(s1)
    if b!=-1:
        print(s1)