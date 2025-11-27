class Node:
    def __init__(self, data):
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
    
    def push_back(self , data):
        new_node = Node(data)
        if(self.head is None and self.tail is None):
            self.head = new_node
            self.tail= new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def pop_front(self):
        if(self.head is None and self.tail is None):
            return
        temp = self.head
        self.head = self.head.next
        del temp
    
    def pop_back(self):
        temp = self.head
        while temp != self.tail:
            temp = temp.next
        del self.tail
        temp.next = None
        self.tail = temp

    def view(self):
        temp = self.head
        while temp != None:
            print(temp.data , end=" -> ")
            temp = temp.next 
    
    def length(self):
        temp = self.head
        size = 0
        while temp != None:
            size += 1
            temp = temp.next 
        return size