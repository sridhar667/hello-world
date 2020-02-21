s =input()
k=int(input())
a = []
count = 0
for i in range(len(s)):
    if s[i] not in a:
        a.append(s[i])
        count += k+3
    else:
        break
print(count)