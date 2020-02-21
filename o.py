s=input()
flag=False
for i in s:
    if i in 'ab':
        flag=True
if flag:
    print('yes')
else:
    print('no')
