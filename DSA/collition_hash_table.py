class Hash_table:
    def __init__(self):
        self.MAX = 10
        self.array = [[] for _ in range(self.MAX)]
        
    def hash(self, key):
        return sum(ord(char) for char in key) % self.MAX
    
    def __setitem__(self, key, value):
        h = self.hash(key)
        found = False

        for idx, element in enumerate(self.array[h]):
            if element[0] == key:
                self.array[h][idx] = (key, value)
                found = True
                break
        
        if not found:
            self.array[h].append((key, value))
                            
    def __getitem__(self, key):
        h = self.hash(key)
        for element in self.array[h]:
            if element[0] == key:
                return element[1]
        raise KeyError(f"{key} not found in hash table.")
    
    def __delitem__(self, key):
        h = self.hash(key)
        for idx, element in enumerate(self.array[h]):
            if element[0] == key:
                del self.array[h][idx]
                return
        raise KeyError(f"{key} not found for deletion.")

    def printlist(self):
        for element in self.array:
            print(element)
    
if __name__ == '__main__':
    table = Hash_table()                       
    table['september 11'] = 2010
    print(table['september 11'])  
    table['march 6'] = 130
    table['march 17'] = 450
    print(table['march 6'])  
    print(table['march 17'])      
    print("Hash table array content:")
    # print(table.array)            
    table.printlist()