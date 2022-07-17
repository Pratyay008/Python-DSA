# ---------------------------------------Linked List basic-----------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end='  ')
            temp = temp.next
        print('\n')


llist = LinkedList()

llist.head = Node(12)       
second = Node(24)       
third = Node(37)       
fourth = Node(49)       


llist.head.next = second
second.next = third
third.next = fourth

llist.printList()


#
# -------------Linked List operations -----------------------------------
# -----------------------1) At the front of the linked list --------------  2) After a given node.
# -------------------- 3) At the end of the linked list.----------------------------
# ------- Deletion in linked list.  from---> beginning , end & middle [in one else: while()]  -------



class Node:
	def __init__(self, data):
		self.data= data
		self.next= None


class LinkedList:
	def __init__(self):
		self.head = None


	def insertBegin(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node


	def insertAfter(self, pre_node, new_data):
		if (pre_node is None):
			print("The given previous node must be in linked list")
		else:
			new_node = Node(new_data)
			new_node.next = pre_node.next
			pre_node.next = new_node
		

	def insertEnd(self, new_data):
		if (self.head is None):
			self.insertBegin(new_data)
		else:	
			new_node = Node(new_data)
			last = self.head
			while(last.next):
				last = last.next
			last.next = new_node	


	def deleteNode(self, key):
		temp = self.head

		if (temp is None):      						 # if()---> not properly running
			print("Item is not present in linked list")
		
		# If the the data/key is present in first node
		elif (temp is not None):
			if (temp.data is key):
				self.head = temp.next
				temp = None
			else:
				while(temp is not None):       # is not ---->  !=
					if(temp.data is key):      # is -------->  ==
						break
					previous = temp	
					temp =temp.next
				previous.next = temp.next
				temp = None

	def printList(self):
		temp = self.head
		print("Now the linked list is : ")
		while (temp):
			print(temp.data, end='  ')
			temp = temp.next
		print('\n')



if __name__=='__main__':
	llist = LinkedList()

	llist.insertAfter(llist.head, 42)
	llist.insertEnd(3)
	llist.printList()

	llist.insertBegin(5)
	llist.printList()
	llist.insertBegin(8)
	llist.insertBegin(9)
	llist.insertBegin(2)
	llist.printList()

	llist.insertAfter(llist.head.next.next,25)
	llist.insertAfter(llist.head,41)
	llist.printList()

	llist.insertEnd(34)
	llist.printList()

	llist.deleteNode(2)
	llist.deleteNode(9)
	llist.printList()






