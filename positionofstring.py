ini_string =input() 
c =input()
res = None
i=0
for i in range(0, len(ini_string)): 
    if ini_string[i] == c: 
        res = i +1
if res == None: 
    print ("No such charater available in string") 
else: 
    print ("Character {} is present at {}".format(c, str(res))) 