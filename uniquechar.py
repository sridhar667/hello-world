n = input()
lst = [int(i) for i in n]
lst = lst[::-1]
lst = map(str,lst)
no = int(''.join(lst))
print(no)   63
