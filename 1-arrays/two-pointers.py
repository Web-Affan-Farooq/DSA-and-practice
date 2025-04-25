lst = [True, False, False, False, True]

def two_pointer(lst:list):
    for i in range(0,len(lst) // 2):
        lst[i],lst[len(lst) -1 - i] = lst[len(lst)-1 - i],lst[i]
    
    return lst

print(two_pointer(lst))

