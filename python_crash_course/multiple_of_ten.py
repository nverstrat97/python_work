# 7-3. a program to determine if a number is a multiple of 10
number = input("Enter a number: ")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")