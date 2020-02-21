n=input()
m=list(map(int,input().split()))
s=m
s.sort()
if s==m:
    print("yes")
else:
    print("no")
  