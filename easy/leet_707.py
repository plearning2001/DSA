class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            temp_node = self.head
            for i in range(index):
                temp_node = temp_node.next
            return temp_node.val
        

    def addAtHead(self, val: int) -> None:
        node = Node(val,self.head)
        self.head = node
        self.size +=1 
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            temp_node = self.head
            while temp_node.next:
                temp_node = temp_node.next
            temp_node.next = node
        
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return -1
        if index < 0:
            index = 0
        if index == 0:
            self.addAtHead(val)
            return

        node = Node(val)
        temp_node = self.head
        for i in range(index-1):
            temp_node = temp_node.next
        node.next = temp_node.next
        temp_node.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            temp_node = self.head
            for i in range(index-1):
                temp_node = temp_node.next
            temp_node.next = temp_node.next.next
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)