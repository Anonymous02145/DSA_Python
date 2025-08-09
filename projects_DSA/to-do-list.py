# Define a Node class to represent each task in the to-do list
class Node:
    def __init__(self, task, deadline, priority):
        self.task = task              # Task name or description
        self.deadline = deadline      # Task deadline
        self.priority = priority      # Task priority (e.g., High, Medium, Low)
        self.next = None              # Pointer to the next node (for linked list)
        self.prev = None              # Pointer to the previous node (for doubly linked list)


# Define the TO_DO class to manage the to-do list
class TO_DO:
    def __init__(self):
        self.head = None              # Head pointer to the start of the list
        self.Max = 20                 # Optional limit for max number of tasks

    # Method to add a new task to the beginning of the list
    def create(self, task, deadline, priority):
        node = Node(task, deadline, priority)  # Create a new node with given details
        node.next = self.head                  # Point the new node to current head

        if self.head is not None:              # If the list isn't empty
            self.head.prev = node              # Set the previous head's prev to new node

        self.head = node                       # Update the head to the new node
        return self.head                       # Return the new head

    # Method to count and print number of tasks
    def count(self):
        count = 0
        if self.head is None:                  # If list is empty
            print("List is empty")
            return 0

        current = self.head                    # Start from head
        while current is not None:             # Traverse the list
            count += 1
            current = current.next

        print("Total Tasks >", count)          # Print total count
        return count                           # Return count

    # Same as count() but without printing anything
    def number(self):
        count = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:
            count += 1
            current = current.next

        return count

    # Method to display all tasks in the list
    def show(self):
        if self.head is None:
            print("List is empty")
            return

        item = self.head                       # Start from head
        while item:                            # Traverse the list
            print({
                "Task": item.task,
                "Deadline": item.deadline,
                "Priority": item.priority
            })
            item = item.next

    # Method to search for a specific task by name
    def fetch(self, target):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current is not None:             # Traverse the list
            if current.task == target:         # If task matches target
                task_details = {
                    "Task": current.task,
                    "Deadline": current.deadline,
                    "Priority": current.priority
                }
                print(task_details)            # Print the task details
                return task_details
            current = current.next

        print(f"Task '{target}' not found.")   # If task not found
        return None

    # Method to sort tasks based on priority
    def sort_by_priority(self):
        if self.head is None:
            print("List is empty")
            return

        # Step 1: Extract nodes into a list for easier sorting
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next

        # Step 2: Define the sorting order for priorities
        priority_order = {'High': 1, 'Medium': 2, 'Low': 3}

        # Step 3: Sort the list of nodes using priority values
        nodes.sort(key=lambda node: priority_order.get(node.priority, 4))

        # Step 4: Rebuild the doubly linked list with sorted nodes
        self.head = nodes[0]            # Set new head to the first sorted node
        self.head.prev = None           # First node's prev should be None

        for i in range(len(nodes) - 1): # Re-link each node to the next one
            nodes[i].next = nodes[i + 1]
            nodes[i + 1].prev = nodes[i]

        nodes[-1].next = None           # Last node's next should be None

        print("Tasks sorted by priority:")
        self.show()                     # Display the sorted list


# ----------------------------
# Example usage
# ----------------------------
if __name__ == '__main__':
    Manager = TO_DO()  # Create an instance of the TO_DO manager

    # Add tasks with different priorities
    Manager.create("Study", "13/08/2010", "High")
    Manager.create("Hack", "14/08/2010", "Low")
    Manager.create("Code", "15/08/2010", "Medium")
    Manager.create("Stalk", "16/08/2010", "High")

    Manager.fetch("Study")       # Fetch and display a task named "Study"
    Manager.count()              # Print the total number of tasks
    Manager.sort_by_priority()   # Sort tasks by their priority and display them
