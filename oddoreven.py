n = input()
lst = [int(i) for i in n]
for i in lst:
    if i%2==0:
        lst.remove(i)
s = sum(lst)
if s%2==0:
    print('Even')
else:
    print('Odd')
    
    