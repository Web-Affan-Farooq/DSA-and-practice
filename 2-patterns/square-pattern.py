n = 3
spaces = 0

for i in range(0,n):
    string = ""
    for j in range(0,n):
        string += " "*spaces + str(i)
        
    print(string)    
# ___Floyd's triangle patterns (very important)
"""
1,
2,3,
4,5,6,
7,8,9,10,
"""
# n = 5
# num = 1

# for i in range(1,n):
#     string = ""
#     for j in range(0,i):
#         string += str(num) +","
#         num +=1
    
#     print(string)
    

# Pattern-1
"""
*
**
***
****
*****
"""
# n = 5
# for i in range(0,n):
#     string = ""
    
#     for j in range(i):
#         string +="*"
    
#     print(string)


#  __ Incrementing square pattern
"""
1,2,3
4,5,6
7,8,9
10,11,12,
13,14,15
"""
# n = 4
# num = 1
# for i in range(0,n):
#     string = ""
#     for j in range(0, n):
#         string+=str(num) + " , "
#         num +=1
#     print(string)


"""
*****
****
***
**
*
"""
# n = 5
# for i in range(n,0,-1):
#     string = ""
    
#     for j in range(i):  
#         string +="*"

#     print(string)