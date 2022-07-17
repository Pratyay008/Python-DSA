class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def insertElement(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)    
            self.last_node = self.last_node.next  
            self.last_node.next = self.head


    def printList(self):
        print("Now the linked list is : ", end='')
        current = self.head            
        # while current is not None:                # same as below
        while (current is not None):
            print(current.data, end='   ')                
            current = current.next
            if current is self.head:
                break
        print()        
        print()        





l1 = CircularLinkList()
l1.insertElement(5)
l1.insertElement(6)
l1.insertElement(8)
l1.insertElement(9)

l1.printList()













