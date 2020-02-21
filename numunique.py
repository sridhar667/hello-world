n=int(input())
li=list(map(int,input().split()))[:n]
for i in li:
  if i in li[i:]:
    print(i)
    break
else:
  print("unique")