class Policy:
    def __init__(self, line):

        splitLine = line.strip().split(' ')
        self.character = splitLine[1].strip()
        
        numbers = splitLine[0].split('-')

        self.min = int(numbers[0].strip())
        self.max = int(numbers[1].strip())

    def toString(self):
        print(self.character)
        print(self.min)
        print(self.max)

    def isValidPassword(self, password):
        characterCount = password.count(self.character)
        if characterCount < self.min or characterCount > self.max:
            return False
        
        return True

