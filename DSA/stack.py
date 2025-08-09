#stack is a data structure common in process shedulers.
from collections import deque

class Stack:
    def __init__(self):
        self.value = None
        self.stack = deque()
        
    def push(self, val):
        return self.stack.append(val)
    
    def pop(self):
        return self.stack.pop()
    
    def show(self):
        for element in self.stack:
            print(element)
            
    def is_empty(self):
        empty = False
        if len(self.stack) == 0:
            empty = True
        
        print(empty)
        
if __name__ == '__main__':
    stack = Stack()
    