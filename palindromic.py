n = int(input())
arr = list(map(int, input().split()))

if n % 2 == 0:
    m1 = n//2 - 1
    m2 = m1+1
else:
    m1 = n//2-1
    m2 = m1+2
while arr[m1] == arr[m2] and m1 > 0 and m2 < n:
    m1 -= 1
    m2 += 1
    print(m1,m2)
if m1 >= 0 and m2 < n:
    if arr[m1] > arr[m2]:
        arr[m2] = arr[m1]
    else:
        arr[m1] = arr[m2]
    m1 -= 1
    m2 += 1
    while m1 >= 0 and m2 < n:
        arr[m2] = arr[m1]
        m1 -= 1
        m2 += 1
print(''.join(str(i) for i in arr))