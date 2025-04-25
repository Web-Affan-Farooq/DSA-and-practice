def find_unique(lst:list):
    dictionary = {}
    for i in range(0, len(lst)):
        if(lst[i] in dictionary.keys()):
            dictionary[lst[i]] +=1
        else :
            dictionary[lst[i]] = 0
            
    unique = []
    for item in dictionary:
        if(dictionary[item] == 0):
            unique.append(item)
        
    return unique
print(find_unique([2,2,2,2,2,1,2,4]))            