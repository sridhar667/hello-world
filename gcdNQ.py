def gcd(x, y): 
  while(y): 
    x, y = y, x % y 
  return x 
n,k = map(int,input().split())
a= list(map(int,input().split()))
b=[]
for i in range(k):
  c,d = map(int,input().split())
  b.append([c,d])
c=[]
for i in range(k):
  d = a[b[i][0]-1:b[i][1]+1]
  x=d[0] 
  y=d[1] 
  g=gcd(x,y) 
  for i in range(2,len(d)): 
      g=gcd(g,d[i]) 
  if len(d)==1:
    c.append(a[b[i][0]-1])
  else:
    c.append(g)	
for i in range(k):
  print(c[i])