from LinkedList import LinkedList

class ReverseLinkList(LinkedList):
    def __init__(self):
        super().__init__()
    
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

lst = ReverseLinkList()
for i in range(1,4):
    lst.push_back(i)
print("before : ")
lst.view()
print("\nafter : ")
lst.reverse()
lst.view()
                    