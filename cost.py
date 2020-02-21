x,y = map(str,input().split())
l1 = len(x)
l2 = len(y)
if l1>l2:
	print(l1-l2)
else:
  	print(l2-l1)