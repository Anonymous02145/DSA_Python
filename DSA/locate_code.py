cards = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
query = int(input("Enter the query card > "))

for i in cards:
    if i == query:
        print(i)
        print("Found at index >> ", cards.index(i))
        
