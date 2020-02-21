def isArmstrong(val:int) -> bool:  
    parts = [int(_) for _ in str(val)]  
    counter = 0
    for _ in parts: 
        counter += _**3
    return ( counter == val )   
print(isArmstrong(100)) 
print(isArmstrong(153)) 
print([ _ for _ in range(1000) if isArmstrong(_)]) 