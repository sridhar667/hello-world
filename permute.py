from itertools import permutations 
  
def allPermutations(str): 
       
     # Get all permutations of string 'ABC' 
     permList = permutations(str) 
     
     # print all permutations 
     for perm in list(permList):
         l=[] 
         l.append(''.join(perm)) 
     l.sort()
     
     print(l[h+1])  
# Driver program 
 
str = input()
allPermutations(str) 