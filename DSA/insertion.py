class Insertion:

    def __init__(self, array : list):
        self.array = array

    def sort(self):
        n = len(self.array)

        for i in range(1, n):
            key = self.array[i]
            j = i - 1

            while j >= 0 and self.array[j] > key:
                self.array[j+1] = self.array[j]
                j -= 1

            self.array[j+1] = key

        return self.array

if __name__ == '__main__':

    numbers = [3, 8, 23, 98 , 86, 99, 100, 938 , 93334, 93845]
    insertion = Insertion(numbers)
    print(insertion.sort())