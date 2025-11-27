## Merge 2 sorted linked list :
from LinkedList import LinkedList

class MergeLinkedList(LinkedList):
    def __init__(self):   
        super().__init__();

    def merge(self , head_1:Node , head_2:Node):
        if head_1 is None:
            return head_2
        elif head_2 is None:
            return head_1
        elif head_1 is None and head_2 is None:
            return
        elif head_1.data <= head_2.data:
            head_1.next= self.merge(head_1.next , head_2)
            return head_1
        elif head_1.data > head_2.data:
            head_2.next = self.merge(head_1 , head_2.next)
            return head_2
        
lst_1= MergeLinkedList()
lst_2= LinkedList()

for i in range(1,4):
    lst_1.push_back(i)

for i in range(1,4):
    lst_2.push_back(i)

result = lst_1.merge(lst_1.head , lst_2.head)
while result is not None:
    print(result.data , end=" -> ")
    result = result.next