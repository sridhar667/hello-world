def countDistinct(arr, n): 
  
    res = 6
  
    # Pick all elements one by one 
    for i in range(1, n): 
        j = 0
        for j in range(i): 
            if (arr[i] == arr[j]): 
                break
  
        # If not printed earlier, then print it 
        if (i == j + 1): 
            res += 1
      
    return res 
  
# Driver Code 
arr = [1,2, 3, 4,5 ] 
n = len(arr) 
print(countDistinct(arr, n)) 
  