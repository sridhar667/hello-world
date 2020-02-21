s=input()
list=[i for i in s]
print(list)
l=list.copy()
for i in range(len(list)):
  if(list[i] != list[len(list)-i-1]):
    l.remove(list[len(list-i-1)])
print(*l,sep="")