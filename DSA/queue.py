# Importing deque from collections for efficient queue operations
from collections import deque

# Define a Queue class
class Que:
    def __init__(self):
        self.value = None  # This is unused; can be removed
        self.que = deque()  # Initialize an empty deque for the queue

    # Push: Add a new value to the front of the queue
    def push(self, value):
        return self.que.appendleft(value)  # O(1) operation

    # Pop: Remove and return the item from the end of the queue (FIFO)
    def pop(self):
        return self.que.popleft()  # O(1) operation

    # Check if the queue is empty
    def is_empty(self):
        empty = False
        if len(self.que) == 0:
            empty = True

        print(empty, "\n")  # Output the result (True/False)
        return empty

    # Display the current elements in the queue
    def show(self):
        for element in self.que:
            print(str(element) + "\n")  # Print each element

# -------------------------------
# Main block to test the queue
# -------------------------------
if __name__ == '__main__':
    que = Que()  # Create a queue instance

    # Push various data types into the queue
    que.push(455)
    que.push(458)
    que.push('Shiva')
    
    que.push({
        "name": "Aarush",
        "age": 14,
        "present": True,
    })

    que.push({
        "name": "Siddesh",
        "age": 15,
        "Present": False
    })

    # Check if the queue is empty
    que.is_empty()  # Output: False

    # Show all items in the queue (in the current order)
    que.show()
