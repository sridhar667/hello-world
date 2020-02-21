n = int(input())
lst = list(map(int,input().split()))
fin = '*'
for i in lst:
    if lst.count(i)>1:
        fin = i
        break
if fin!='*':
    print(fin)
else:
    print('unique')
    