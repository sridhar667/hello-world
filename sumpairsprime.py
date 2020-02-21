def findPairs(lst, K):  
    res = [] 
    while lst: 
        num = lst.pop() 
        diff = K - num 
        if diff in lst: 
            res.append((diff, num)) 
    res.reverse() 
    return len(res) 
   

lst = [2,3,5,7] 
K =int(input())
c = 0
for i in range (len(lst)):
    if K==lst[i]+lst[i]:
        c+=1
print(findPairs(lst, K)+c)