def read_input():
    numbers = []
    input_file = open('input.txt', 'r') 

    for line in input_file:
        numbers.append(int(line))
    input_file.close()

    return numbers

expectedSum = 2020
numbers = read_input()
numbers.sort()

i = len(numbers) - 1

top = 0
bottom = 0

while i > 0 and bottom == 0:
    top = numbers[i]
    difference = int(expectedSum - top)
    j = 0
    while j < i and numbers[j] < difference:
        j += 1
    if numbers[j] == difference:
        bottom = numbers[j]
        print(top)
        print(bottom)
    i -= 1

print( top * bottom )


