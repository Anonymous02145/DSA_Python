# Binary Search Algorithm to find a target element in a sorted array
# Time Complexity: O(log n), where n is the number of elements in the list

def binary_search(cards, target):
    low = 0
    high = len(cards) - 1

    while low <= high:
        mid = (low + high) // 2  # Get the middle index

        if cards[mid] == target:
            return mid  # Target found at mid index
        elif cards[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found

# Sample sorted list
cards = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Taking input from user
try:
    target = int(input("Enter target > "))
except ValueError:
    print("Please enter a valid integer.")
    exit()

# Perform search
index = binary_search(cards, target)

# Output result
if index != -1:
    print(f"Found at index > {index}")
else:
    print("Target not found.")
