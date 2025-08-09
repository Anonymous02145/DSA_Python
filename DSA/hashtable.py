class Hash_table:
    def __init__(self):
        self.MAX = 10
        self.array = [None for i in range(self.MAX)]
        
    def hash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
            
        return sum % self.MAX
    
    def __setitem__(self, key, value):
        
        hash = self.hash(key)
        self.array[hash] = value
        
    def __getitem__(self, key):
        hash = self.hash(key)
        print(self.array[hash])
    
    def __deleteitem__(self, key):
        hash = self.hash(key)
        print("deleted element at > ", self.array[hash])
        self.array[hash] = None 
       
if __name__ == '__main__':
    table = Hash_table()
    table.hash('myname')
    table['march 6'] = 130
    table['september 11'] = 2010
    table['september 11']
    table['march 6']
        