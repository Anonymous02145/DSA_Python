# Stack is a data structure used widely in process schedulers, expression evaluation, etc.
# It works on LIFO principle: Last In, First Out.

from collections import deque  # Import deque for efficient stack operations (O(1) push/pop)

class Stack:
    def __init__(self):
        # Initialize the stack using deque, which supports fast appends and pops from right end.
        self.stack = deque()
    
    def push(self, val):
        """
        Push (add) a value onto the top of the stack.
        Time Complexity: O(1)
        """
        self.stack.append(val)
    
    def pop(self):
        """
        Pop (remove and return) the topmost element from the stack.
        Raises IndexError if stack is empty.
        Time Complexity: O(1)
        """
        if self.is_empty():
            print("Stack is empty, cannot pop.")
            return None
        return self.stack.pop()
    
    def peek(self):
        """
        Returns the top element of the stack without removing it.
        Returns None if stack is empty.
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def show(self):
        """
        Print all elements in the stack from bottom to top.
        Time Complexity: O(n), where n is number of elements.
        """
        if self.is_empty():
            print("Stack is empty.")
            return
        print("Stack contents (bottom -> top):")
        for element in self.stack:
            print(element)
    
    def is_empty(self):
        """
        Check if the stack is empty.
        Returns True if empty, False otherwise.
        Time Complexity: O(1)
        """
        empty = len(self.stack) == 0
        print(empty)
        return empty


if __name__ == '__main__':
    stack = Stack()  # Create a new stack instance

    # Push some elements onto the stack
    stack.push("Process1")
    stack.push("Process2")
    stack.push(101)
    stack.push({"id": 1, "priority": "High"})

    # Display stack contents
    stack.show()

    # Check if stack is empty
    print("\nIs stack empty?")
    stack.is_empty()

    # Peek the top element
    print("\nPeek top element:")
    print(stack.peek())

    # Pop the top element and display it
    print("\nPopped element:")
    print(stack.pop())

    # Show updated stack contents after pop
    print("\nStack after pop:")
    stack.show()
