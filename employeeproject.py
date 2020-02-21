n=input()
p1=list(map(int,input().split()))
m=input()
p2=list(map(int,input().split()))
l=0
for i in range(0,len(p2)):
    if (p2[i] not in p1 ):
        l=1
        break
    if(l==0):
      print("yes")
      break
    else:
      print("no")