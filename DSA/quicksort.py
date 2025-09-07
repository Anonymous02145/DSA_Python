class Quicksort:
    def __init__(self, array):
        self.array = array

    def hoare_sort(self, low=0, high=None):
        if high is None:
            high = len(self.array) - 1

        if low < high:
            p = self.partition(low, high)
            self.hoare_sort(low, p)
            self.hoare_sort(p + 1, high)

    def partition(self, low, high):
        pivot = self.array[low]
        left = low - 1
        right = high + 1

        while True:
            # Move right until we find a value >= pivot
            while True:
                left += 1
                if self.array[left] >= pivot:
                    break

            # Move left until we find a value <= pivot
            while True:
                right -= 1
                if self.array[right] <= pivot:
                    break

            # If pointers cross, return the right index
            if left >= right:
                return right

            # Swap values at left and right
            self.swap(left, right)

    def swap(self, a, b):
        if a != b:
            self.array[a], self.array[b] = self.array[b], self.array[a]

# Usage
if __name__ == '__main__':
    array = [5, 9, 3, 45, 36, 20]
    sorter = Quicksort(array)
    sorter.hoare_sort()
    print("Sorted array:", sorter.array)
