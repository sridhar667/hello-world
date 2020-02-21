def binomialCoeff(n, k): 
    res = 1; 
  
     
    if (k > n - k): 
        k = n - k
  
    
    for i in range(k):  
        res *= (n - i)
        res /= (i + 1) 
  
    return int(res)
  

def catalan(n): 
      
     
    c = binomialCoeff(2 * n, n)
  
   
    return int(c / (n + 1)); 
  
 
def findWays(n): 
      
    
    if(n & 1): 
        return 0; 
  
    
    return catalan(int(n / 1)); 
  

n =input()
print(findWays(2))