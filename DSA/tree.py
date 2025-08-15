class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def remove_child(self, child):
        print(self.children.remove(child))
        
electronics = Tree("Electronics")
laptops = Tree("Laptops")
