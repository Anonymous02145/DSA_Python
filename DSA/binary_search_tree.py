class BinarySearchTree:
    def __init__(self, data):
        """
        Initialize a BST node with the given data.
        Initially, left and right children are None.
        """
        self.data = data
        self.left = None
        self.right = None
        
    def add_child_node(self, data):
        """
        Insert a new node with the given data into the BST.
        """
        # Ignore duplicates
        if data == self.data:
            return
        
        # If data is smaller, go to the left subtree
        if data < self.data:
            if self.left:
                # Recursively add to the left subtree
                self.left.add_child_node(data)
            else:
                # If left child doesn't exist, create it
                self.left = BinarySearchTree(data)
        else:
            # If data is larger, go to the right subtree
            if self.right:
                self.right.add_child_node(data)
            else:
                self.right = BinarySearchTree(data)
                
    def in_order_traversal(self):
        """
        Return a sorted list of all elements in the BST
        (left, root, right).
        """
        elements = []
        
        # Traverse left subtree
        if self.left:
            elements += self.left.in_order_traversal()
        
        # Visit root
        elements.append(self.data)
        
        # Traverse right subtree
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
              
    def search(self, data):
        """
        Search for a value in the BST.
        Return True if found, else False.
        """
        if data == self.data:
            return True
        
        if data < self.data:
            # Search in left subtree
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            # Search in right subtree
            if self.right:
                return self.right.search(data)
            else:
                return False
            
def build(elements: list):
    """
    Build a BST from a list of elements.
    The first element becomes the root.
    """
    root = BinarySearchTree(elements[0])
    for element in elements[1:]:
        root.add_child_node(element)
    return root    

# ------------------- Usage -------------------

if __name__ == '__main__':
    numbers = [1, 4, 8, 9, 10, 3, 26, 76]
    
    # Build the initial BST
    root = build(numbers)
    
    # Search for a value
    print(root.search(4))  # True
    print(root.search(100))  # False
    
    # Print sorted elements
    print(root.in_order_traversal())  # [1, 3, 4, 8, 9, 10, 26, 76]
    
    # Insert a new element
    root.add_child_node(30)
    
    # Check updated BST
    print(root.in_order_traversal())  # [1, 3, 4, 8, 9, 10, 26, 30, 76]
