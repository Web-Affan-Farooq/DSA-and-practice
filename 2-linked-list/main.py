class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_front(self, data):
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
    
    def pop_front(self):
        if self.head is None:
            pass
        
        temp = self.head
        self.head = self.head.next
        del temp
    
    def push_back(self , data):
        new_node = Node(data)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return 

        self.tail.next = new_node
        self.tail = new_node
    
    def pop_back(self):
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        
        temp.next = None
        del self.tail
        self.tail = temp
    
    def insert(self , position:int , data):
        new_node = Node(data)
        
        temp = self.head
        for i in range(1,position-1):
            temp = temp.next
        new_node.next = temp.next.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data , end=" -> ")
            temp = temp.next

lst = LinkedList()
lst.push_back(1)
lst.push_back(2)
lst.push_back(3)
lst.insert(2, 10)
lst.display()