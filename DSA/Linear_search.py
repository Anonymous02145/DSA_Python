# List of cards in descending order
cards = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Ask the user to input the card they are searching for
query = int(input("Enter the query card > "))

# Flag to track if the card is found
found = False

# Linear search: iterate through each card in the list
for i in range(len(cards)):
    if cards[i] == query:
        print("Card Found:", cards[i])
        print("Found at index >>", i)
        found = True
        break  # Exit the loop once the card is found

# If not found, inform the user
if not found:
    print("Card not found in the list.")
