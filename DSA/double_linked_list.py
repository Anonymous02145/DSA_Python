class Node:
    def __init__(self, data = 0):
        self.next = None
        self.prev = None 
        self.data = data
        
    

class Double_Linked_List:
    
    def __init__(self):
        self.head = None 
    
    def insert_begining(self, data):
        node = Node(data)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
            
        self.head = node
        return self.head 
        
    def insert_at_middle(self, data, next = self.insert_at_middle(), prev = self.insert_begining()):
        middle_node = Node(data, next, prev)
        
        