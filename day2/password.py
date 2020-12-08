from policy import Policy

class Password:
    def __init__(self, line):
        line = line.split(':')
        self.policy = Policy(line[0])
        self.password = line[1].strip()

    def toString(self):
        self.policy.toString()
        print(self.password)

    def isValid(self):
        return self.policy.isValidPasswordV2(self.password)
