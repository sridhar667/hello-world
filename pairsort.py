def getPairsCount(arr, n, sum): 
      
    count = 0 
    for i in range(0, n): 
        for j in range(i + 1, n): 
            if arr[i] - arr[j] == k: 
                count += 1
      
    return count 
  
n,k=input().split()  
arr =list(map(int,input().split())) 
print("Count of pairs is", 
      getPairsCount(arr, n, k)) 