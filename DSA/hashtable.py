# Define the Hash_table class
class Hash_table:
    def __init__(self):
        self.MAX = 10  # Set the size of the internal array
        self.array = [None for _ in range(self.MAX)]  # Initialize the array with None

    # Hash function: Converts a string key into a valid index
    def hash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)  # Get ASCII value of each character and sum them
        return sum % self.MAX  # Return index within bounds of array

    # Method to insert or update a key-value pair using bracket syntax
    def __setitem__(self, key, value):
        h = self.hash(key)  # Get hash index for the key
        self.array[h] = value  # Store the value at the computed index

    # Method to retrieve a value using bracket syntax
    def __getitem__(self, key):
        h = self.hash(key)  # Get hash index for the key
        print(self.array[h])  # Print the value stored at that index

    # ❌ Incorrectly named: __deleteitem__ is not a recognized magic method
    # ✅ Correct name should be: __delitem__
    def __delitem__(self, key):
        h = self.hash(key)  # Get hash index for the key
        print("Deleted element at index", h, "with value >", self.array[h])
        self.array[h] = None  # Remove the element (set it to None)

# --------------------------------------
# Main program: Demonstrates usage
# --------------------------------------
if __name__ == '__main__':
    table = Hash_table()  # Create a hash table instance

    table.hash('myname')  # Hashing a key just to test the function (returns index)

    # Add some key-value pairs
    table['march 6'] = 130
    table['september 11'] = 2010

    # Retrieve and print values using keys
    table['september 11']  # Expected output: 2010
    table['march 6']       # Expected output: 130
