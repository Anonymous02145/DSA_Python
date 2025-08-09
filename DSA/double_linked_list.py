# Node class represents each element in the doubly linked list
class Node:
    def __init__(self, data=0):
        self.next = None       # Pointer to the next node
        self.prev = None       # Pointer to the previous node
        self.data = data       # Data stored in the node


# Double_Linked_List manages the list operations
class Double_Linked_List:
    def __init__(self):
        self.head = None       # Head (start) of the list

    # Insert a new node at the beginning of the list
    def insert_beginning(self, data):
        node = Node(data)      # Create a new node with the given data
        node.next = self.head  # New node points to current head

        if self.head is not None:
            self.head.prev = node  # If list isn't empty, update previous head's prev pointer

        self.head = node       # Update head to the new node
        return self.head

    # Count number of nodes in the list
    def count(self):
        current = self.head    # Start at head
        count = 0              # Counter to keep track of nodes

        while current:
            count += 1
            current = current.next  # Move to next node

        return count           # Return total count

    # Insert a new node at the middle of the list
    def insert_at_middle(self, data):
        # If the list is empty, insert at beginning
        if self.head is None:
            self.insert_beginning(data)
            return

        length = self.count()           # Get total number of nodes
        mid_index = length // 2         # Determine middle index

        current = self.head
        for _ in range(mid_index):      # Traverse to the middle node
            current = current.next

        # Create a new node to insert before the current node
        new_node = Node(data)
        prev_node = current.prev        # Get the previous node

        # Set pointers for the new node
        new_node.next = current         # new_node.next points to current
        new_node.prev = prev_node       # new_node.prev points to previous node

        # Update surrounding nodes to point to the new node
        if prev_node:
            prev_node.next = new_node   # Link previous node to new node
        current.prev = new_node         # Link current node back to new node

        # If we are inserting at index 0, update the head
        if current == self.head:
            self.head = new_node

    # Display the full list from head to end
    def display(self):
        current = self.head             # Start from the head
        while current:
            print(current.data, end=" <-> ")  # Print current node's data
            current = current.next      # Move to the next node
        print("None")                   # Indicate the end of the list


# ----------------------------
# Example usage
# ----------------------------
if __name__ == '__main__':
    dll = Double_Linked_List()

    # Inserting nodes at the beginning
    dll.insert_beginning(50)
    dll.insert_beginning(40)
    dll.insert_beginning(30)
    dll.insert_beginning(20)
    dll.insert_beginning(10)

    print("Before inserting at middle:")
    dll.display()  # Output current list

    dll.insert_at_middle(999)  # Insert 999 in the middle

    print("After inserting 999 in the middle:")
    dll.display()  # Output updated list
