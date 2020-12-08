from password import Password

def read_input():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines



lines = read_input()

validCount = 0

for line in lines:
    password = Password(line)
    if password.isValid():
        validCount += 1
        
print(validCount)

# password = Password('7-10 m: hsdgdmmqqncdcgfxpb')
# password.toString()
# print(password.isValid())