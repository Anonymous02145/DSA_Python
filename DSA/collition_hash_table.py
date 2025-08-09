class HashTable:
    def __init__(self):
        self.MAX = 10  # Size of the hash table
        self.array = [[] for _ in range(self.MAX)]  # Initialize with empty buckets (lists)

    def hash(self, key):
        # Hash function: sum of ASCII values of characters modulo MAX size
        return sum(ord(char) for char in key) % self.MAX

    def __setitem__(self, key, value):
        h = self.hash(key)  # Calculate the hash index
        found = False

        # Check if the key exists and update the value if it does
        for idx, element in enumerate(self.array[h]):
            if element[0] == key:
                self.array[h][idx] = (key, value)  # Update key-value pair
                found = True
                break

        if not found:
            self.array[h].append((key, value))  # Insert new key-value pair

    def __getitem__(self, key):
        h = self.hash(key)
        for element in self.array[h]:
            if element[0] == key:
                return element[1]  # Return the value for the key
        raise KeyError(f"{key} not found in hash table.")  # Key doesn't exist

    def __delitem__(self, key):
        h = self.hash(key)
        for idx, element in enumerate(self.array[h]):
            if element[0] == key:
                del self.array[h][idx]  # Delete the key-value pair
                return
        raise KeyError(f"{key} not found for deletion.")  # Key doesn't exist

    def printlist(self):
        for i, element in enumerate(self.array):
            print(f"Bucket {i}: {element}")


# ----------------------------
# Example usage
# ----------------------------
if __name__ == '__main__':
    table = HashTable()

    # Insert key-value pairs
    table['september 11'] = 2010
    print(table['september 11'])  

    table['march 6'] = 130
    table['march 17'] = 450

    # Retrieve values
    print(table['march 6'])  
    print(table['march 17'])      

    print("\nHash table array content:")
    table.printlist()
