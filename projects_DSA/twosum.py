class Magic:
    def __init__(self, numbers):
        self.numbers = numbers
        
    def magic_numbers(self, target):
        seen = {}
        
        for index, number in enumerate(self.numbers):
            compliment = target - number
            
            if compliment in seen:
                return (seen[compliment], index)
            
            seen[number] = index
            
if __name__ == '__main__':
    numbers = [2, 9, 8, 6, 4, 3, 1, 10]
    magic_number = Magic(numbers=numbers)
    print(magic_number.magic_numbers(11))
