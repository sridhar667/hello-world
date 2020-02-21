s = input()
n = len(s)
flag = True
while flag :
    flag = False
    i=0
    while i < n :
        if s[i] == '[' :
            i2 = i
            i += 1
        elif s[i] == ']' :
            k = int(s[i2-1])
            s = s[:i2-1] + s[i2+1:i] * k + s[i+1:]
            n = len(s)
            flag = True
            i += 1
            
        else :
            i += 1
print(s,end='')

