numbers = list(range(1, 1000001))
# this prints the sum of all the numbers from 1 to 1,000,000
print(sum(numbers))

# this prints the minimum number in the list
print(min(numbers))
# this prints the maximum number in the list
print(max(numbers))

odd_numbers = []
for value in range(1, 20, 2):
    odd_numbers.append(value)
    print(value)
print(odd_numbers)

threes = []
for value in range(3, 31, 3):
    threes.append(value)
    print(value)
print(threes)

cubes = [value**3 for value in range(1, 11)]
print(cubes)
# End of script