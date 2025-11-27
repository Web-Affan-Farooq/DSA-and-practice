from LinkedList import LinkedList

class LinkedListMiddle(LinkedList):
    def __init__(self):
        super().__init__()
    
    def middle(self):
        size = self.length()
        temp = self.head
        for i in range(size // 2 ):
            temp = temp.next
        return temp.data


lst = LinkedListMiddle()
for i in range(1,5):
    lst.push_back(i)

lst.view()
print("\n" ,lst.middle())