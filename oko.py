s1,s2=map(str,input().split())
count=0
for i in range(len(s1)):
    if s1[i]!=s2[i]:
        count=count+1
if count==1:
    print("yes")
else:
    print("no")