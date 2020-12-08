def read_input():
    numbers = []
    input_file = open('input.txt', 'r') 

    for line in input_file:
        numbers.append(int(line))
    input_file.close()

    return numbers

def find_two_numbers(numbers, index, expectedSum):
    i = index

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
    
    return top * bottom



expectedSum = 2020
numbers = read_input()
numbers.sort()

i = len(numbers) - 1

first = 0
multiplicationResult = 0

while i > 0 and multiplicationResult == 0:
    first = numbers[i]
    difference = int(expectedSum - first)
    multiplicationResult = find_two_numbers(numbers, i - 1, difference)
    if multiplicationResult > 0:
        print(first)
    i -= 1

print( first * multiplicationResult )


