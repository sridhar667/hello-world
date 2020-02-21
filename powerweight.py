n = input()
lst = [int(i) for i in n]
c=0
s=0
for i in lst:
    s+=i**c
    c+=1
print(s)
