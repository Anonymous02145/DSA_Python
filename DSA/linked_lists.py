# Node class represents each element (node) in the linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data  # Holds the value for the node
        self.next = next  # Points to the next node in the list


# LinkedList class manages the list operations
class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty (head is None)

    # Insert a new node at the beginning of the list
    def insert_begining(self, data):
        # Create a new node with the current head as its next node
        node = Node(data, self.head)
        # Update the head to point to the new node
        self.head = node

    # Count the number of nodes in the list
    def count(self):
        count = 0
        _list = self.head  # Start from head

        while _list:       # Traverse until the end
            count += 1     # Increment counter
            _list = _list.next  # Move to the next node

        print(count)       # Print total number of nodes

    # Print the entire linked list
    def printlist(self):
        if self.head is None:
            print("List None")  # If list is empty
            return

        itr = self.head      # Iterator to traverse the list
        llstr = ''           # String to store formatted list

        while itr:
            llstr += str(itr.data) + '-->'  # Append data to string
            itr = itr.next

        print(llstr)         # Print the final linked list string

    # Insert a new node at the end of the list (tail)
    def insert_at_tail(self, data):
        new_node = Node(data)  # Create a new node

        if self.head is None:
            self.head = new_node  # If list is empty, new node becomes head
            return

        last = self.head
        while last.next:         # Traverse to the last node
            last = last.next

        last.next = new_node     # Append the new node at the end

    # Search for a target value in the list
    def search(self, target):
        _search = self.head  # Start from the head

        while _search:
            if _search.data == target:  # If target is found
                print("Found", target, " > ", True)
                return True
            _search = _search.next      # Move to next node

        # Optional: You can print not found (not in original code)
        # print("Not Found", target)
        # return False


# ----------------------------
# Example usage
# ----------------------------
if __name__ == '__main__':
    link = LinkedList()               # Create linked list instance

    # Insert nodes at the beginning
    link.insert_begining(13)
    link.insert_begining(24)
    link.insert_begining(88)

    # Insert node at the end
    link.insert_at_tail(23)

    # Search for a value in the list
    link.search(24)

    # Print the full list
    link.printlist()

    # Count number of elements
    link.count()
