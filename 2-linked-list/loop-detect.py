from LinkedList import LinkedList

class LinkedListWithLoop(LinkedList):
    def __init__(self):
        super().__init__()
    
    def create_loop(self, position):
        temp = self.head
        count = 0
        while count != position and temp != None:
            count +=1 
            temp = temp.next
        
        self.tail.next = temp
    
    def detect_loop(self):
        slow = self.head 
        fast = self.head

        while fast != None:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False

lst = LinkedListWithLoop()
for i in range(1,5):
    lst.push_back(i)
lst.view()
lst.create_loop(2)
print(f"Loop exists ? : {lst.detect_loop()}")