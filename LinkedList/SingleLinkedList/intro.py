class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head =  None
        self.tail = None
        self.length =0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
    
    def insert(self,index,value):
        if index <0 or index > self.length:
            return False
        new_node = Node(value)
        temp_node = self.head
        
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        elif index == 0 :
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1
        return True
    
    def __str__(self) ->str:
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None :
                result +='->'
            temp_node = temp_node.next
        return result
                

new_ll = LinkedList()
new_ll.append(10)
new_ll.append(20)
new_ll.append(30)
new_ll.insert(1,50)

print(new_ll)

