class Policy:
    def __init__(self, line):

        splitLine = line.strip().split(' ')
        self.character = splitLine[1].strip()
        
        numbers = splitLine[0].split('-')

        self.min = int(numbers[0].strip())
        self.max = int(numbers[1].strip())

    def toString(self):
        print(self.min, "-", self.max, " ", self.character)

    def isValidPassword(self, password):
        characterCount = password.count(self.character)
        if characterCount < self.min or characterCount > self.max:
            return False
        
        return True

    def isValidPasswordV2(self, password):
        
        characterCount = 0
        if password[self.min - 1] == self.character:
            characterCount += 1
        
        if password[self.max - 1] == self.character:
            characterCount += 1
        
        return characterCount == 1

