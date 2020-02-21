I = int(input())
B = bin(I)[2:]
B = B[::-1]
for i in range(0,len(B)):
    if B[i] == '1':
        P = i+1
        break
print(P)
