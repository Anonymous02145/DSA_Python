class Sort:
    def __init__(self, array : list):
        self.array = array

    def sort(self):
        n = len(self.array)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if self.array[j] < self.array[min_index]:
                    self.array[j], self.array[min_index] = self.array[min_index], self.array[j]

        return self.array

if __name__ == '__main__':
    to_sort = [1, 10, 3, 4, 99, 20]
    sorter = Sort(to_sort)
    print(sorter.sort())
