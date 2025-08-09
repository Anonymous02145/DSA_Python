#Que is used to make a buffer to store the value that is pushed 
from collections import deque

class Que:
    def __init__(self):
        self.value = None 
        self.que = deque()
        
    def push(self, value):
        return self.que.appendleft(value)
    
    def pop(self):
        return self.que.popleft()
    
    def is_empty(self):
        empty = False
        if len(self.que) == 0:
            empty = True
            
        print(empty, "\n")
        return empty
    
    def show(self):
        for element in self.que:
            print(str(element) + "\n")
        
        
if __name__ == '__main__':
    que = Que()
    que.push(455)
    que.push(458)
    que.push('Shiva')
    que.push({
        "name" : "Aarush",
        "age" : 14,
        "present" : True,
    })
        
    que.push({
        "name" : "Siddesh",
        "age" : 15,
        "Present" : False
        })
    
    que.is_empty()
    que.show()
    

