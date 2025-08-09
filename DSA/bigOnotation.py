#BigO notation is used to find the target element in a very big array.
#Need to do k = n/2^k

cards = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

low = 0
high = len(cards) - 1
target = int(input("Enter target > "))

if target in cards :
    while low <= high : 
        mid = (low + high) // 2
        if cards[mid] == target:
            print("Found at index > ", mid)
            break
        elif cards[mid] < target:
            low = mid + 1
            
        else:
            high = mid - 1
            
            