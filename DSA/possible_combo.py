class Possible:
    def __init__(self, n, letters : list):
        self.n = n
        self.letters = letters
        
    def generate_possibilities(self):
       

        def backtrack(current):
            if len(current) == self.n:
                print(current)
                return True

            for letter in self.letters:
                current += letter

                backtrack(current)

                current = current[:-1]
        backtrack("")

if __name__ == '__main__':
    combo = ["a", "b", "c"]
    possible = Possible(2, combo)
    possible.generate_possibilities()