class Node:
    def __init__(self, task, deadline, priority):
        self.task = task
        self.deadline = deadline
        self.priority = priority
        self.next = None
        self.prev = None


class TO_DO:
    def __init__(self):
        self.head = None
        self.Max = 20  # Can be used for limiting task count if needed

    def create(self, task, deadline, priority):
        node = Node(task, deadline, priority)
        node.next = self.head

        if self.head is not None:
            self.head.prev = node

        self.head = node
        return self.head

    def count(self):
        count = 0
        if self.head is None:
            print("List is empty")
            return 0

        current = self.head
        while current is not None:
            count += 1
            current = current.next

        print("Total Tasks >", count)
        return count

    def number(self):
        count = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:
            count += 1
            current = current.next

        return count

    def show(self):
        if self.head is None:
            print("List is empty")
            return

        item = self.head
        while item:
            print({
                "Task": item.task,
                "Deadline": item.deadline,
                "Priority": item.priority
            })
            item = item.next

    def fetch(self, target):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current is not None:
            if current.task == target:
                task_details = {
                    "Task": current.task,
                    "Deadline": current.deadline,
                    "Priority": current.priority
                }
                print(task_details)
                return task_details
            current = current.next

        print(f"Task '{target}' not found.")
        return None

    def sort_by_priority(self):
        if self.head is None:
            print("List is empty")
            return

        # Step 1: Extract nodes into a list
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next

        # Step 2: Define priority mapping
        priority_order = {'High': 1, 'Medium': 2, 'Low': 3}

        # Step 3: Sort nodes based on priority
        nodes.sort(key=lambda node: priority_order.get(node.priority, 4))

        # Step 4: Rebuild the linked list
        self.head = nodes[0]
        self.head.prev = None

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
            nodes[i + 1].prev = nodes[i]

        nodes[-1].next = None

        print("Tasks sorted by priority:")
        self.show()


# ----------------------------
# Example usage
# ----------------------------
if __name__ == '__main__':
    Manager = TO_DO()
    Manager.create("Study", "13/08/2010", "High")
    Manager.create("Hack", "14/08/2010", "Low")
    Manager.create("Code", "15/08/2010", "Medium")
    Manager.create("Stalk", "16/08/2010", "High")

    Manager.fetch("Study")
    Manager.count()
    Manager.sort_by_priority()
