lst = [1,2,3,4,5]
target = 5

def linear_search(lst:list):
    for i in range(0,len(lst)):
        if lst[i] == target:
            return i
    return -1

print(linear_search(lst))