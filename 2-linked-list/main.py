class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def push_front(self , data):
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return 

        new_node.next = self.head
        self.head = new_node
    
    def reverse(self):
        prev = None
        curr = self.head
        next = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head , self.tail = self.tail , self.head
        self.tail.next = None
        self.head = prev
    
    def middle(self):
        temp = self.head
        size = 1
        while temp.next != None:
            size += 1
            temp = temp.next
        
        curr = self.head
        for i in range(size//2):
            curr = curr.next
        
        return curr.data

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data , end=" -> ")
            temp = temp.next 
    
    def create_loop(self , connecting_position):
        temp = self.head 
        for i in range(connecting_position-1):
            temp = temp.next
        
        self.tail.next = temp
    
    def detect_loop(self):
        p1 = self.head
        p2 = self.head

        while p2 != None:
            p1 = p1.next
            p2 = p2.next.next
            if(p1 == p2):
                return True
        
        return False

lst = LinkedList()

for i in range(1,5):
    lst.push_front(i)
lst.create_loop(2)
print(lst.detect_loop())
# lst.display()

# class Node:
#     def __init__(self , data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def push_front(self, data):
#         new_node = Node(data)
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#             return
        
#         new_node.next = self.head
#         self.head = new_node
    
#     def pop_front(self):
#         if self.head is None:
#             pass
        
#         temp = self.head
#         self.head = self.head.next
#         del temp
    
#     def push_back(self , data):
#         new_node = Node(data)

#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#             return 

#         self.tail.next = new_node
#         self.tail = new_node
    
#     def pop_back(self):
#         temp = self.head
#         while temp.next != self.tail:
#             temp = temp.next
        
#         temp.next = None
#         del self.tail
#         self.tail = temp
    
#     def insert(self , position:int , data):
#         new_node = Node(data)
        
#         temp = self.head
#         for i in range(1,position-1):
#             temp = temp.next
#         new_node.next = temp.next.next
#         temp.next = new_node

#     def display(self):
#         temp = self.head
#         while temp != None:
#             # if(temp.next == None):
#             #     print(temp.data , end=" <- ")
#             print(temp.data , end=" -> ")
#             temp = temp.next  
    
#     def search(self , key):
#         if(self.head == None):
#             pass
#         temp = self.head
#         count = 0
#         while temp !=None:
#             if(temp.data == key):
#                 return count
#             temp = temp.next
#             count += 1
#         return -1

#     def reverse(self):
#         prev = None
#         curr = self.head
#         next = None
        
#         while curr != None:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
#         self.head , self.tail = self.tail , self.head
#         self.head = prev
#         self.tail.next = None
#         return prev.data
        
# lst = LinkedList()
# lst.push_back(1)
# lst.push_back(2)
# lst.push_back(3)
# print(f"before : {lst.display()}")
# lst.reverse()
# print(f"after : {lst.display()}")