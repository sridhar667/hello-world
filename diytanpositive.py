def findSmallest(arr, n): 
  
    res = 1 #Initialize result 
  
    # Traverse the array and increment 
    # 'res' if arr[i] is smaller than 
    # or equal to 'res'. 
    for i in range (0, n ): 
        if arr[i] <= res: 
            res = res + arr[i] 
        else: 
            break
    return res

n = int(input())
lst = list(map(int,input().split()))
print(findSmallest(lst, len(lst))) 
