class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class CLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.length = 0
    
    def append(self,value):
        node = Node(value)
        
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node
        else:
            self.tail.next = node
            node.next = self.head
            self.tail = node
        self.length +=1
    
    def prepend(self,value):
        node = Node(value)
        
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node
        else:
            node.next = self.head
            self.head = node
            self.tail.next = node
        self.length +=1
        return
    
    def __str__(self):
        current = self.head
        result = ''
        while current is not None:
            result += str(current.value)
            current = current.next
            
            if current == self.head:
                break
            result += ' -> '
        return result
        
        


cll = CLinkedList()
cll.append(10)
cll.append(20)
print(cll)
cll.prepend(5)
print(cll)