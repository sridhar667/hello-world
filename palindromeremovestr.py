s=input()
list=[i for i in s]
list.pop(len(s)-1)
m=list
m1=list[::-1]
if m==m1:
  print("".join(m))