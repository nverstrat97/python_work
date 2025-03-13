# list of numbers from 1 to 9
numbers = list(range(1, 10))

# loop through the list of numbers to print the ordinal number
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
# Output: numbers 1-9 with their ordinal number