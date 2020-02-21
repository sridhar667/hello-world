n,k=map(int,input().split(" "))
m=list(map(int,input().split()))
count=0
for i in range(0, n): 
        for j in range(0, n):
            if(i != j): 
                if m[i] - m[j] == k: 
                    count += 1
print(count)