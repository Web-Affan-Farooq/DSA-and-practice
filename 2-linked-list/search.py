from LinkedList import LinkedList

class LinkedListWithSearch(LinkedList):
        def __init__(self):
            super().__init__()

        def search(self , data):
            temp = self.head
            count = 0
            while temp != None:
                if(temp.data == data):
                    return count
                count += 1
                temp = temp.next
            return -1

lst = LinkedListWithSearch()
for i in range(1,4):
    lst.push_back(i)
print(lst.search(2))