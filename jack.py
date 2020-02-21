def maxLen(arr): 
      
    # initialize result 
    max_len = 0
  
    # pick a starting point 
    for i in range(len(arr)): 
          
        # initialize sum for every starting point 
        curr_sum = 0
          
        # try all subarrays starting with 'i' 
        for j in range(i, len(arr)): 
          
            curr_sum += arr[j] 
  
            # if curr_sum becomes 0, then update max_len 
            if curr_sum == 0: 
                max_len = max(max_len, j-i + 1) 
  
    return max_len 
  
  
# test array 
n = int(input())
lst = list(map(int,input().split()))
  
print(maxLen(lst))
