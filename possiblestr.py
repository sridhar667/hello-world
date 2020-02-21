def printAllKLength(s, k): 
  
    n = len(s)  
    printAllKLengthRec(s, "", n, k) 
  

def printAllKLengthRec(s, prefix, n, k): 
      
   
    if (k == 0) : 
        print(prefix) 
        return
  
    for i in range(n): 
  
       
        newPrefix = prefix + s[i]
        printAllKLengthRec(s, newPrefix, n, k - 1) 
  
if __name__ == "__main__": 
      

    s,k=list(map(str,input().split()))
    printAllKLength(s, k) 
