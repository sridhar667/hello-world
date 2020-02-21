h = int(input())
c = 1
prev = 1
for i in range(h):
    prev=prev*2
    c+=prev
print(c)
