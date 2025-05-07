# calculator basics
# 3 variables
print("version 1")
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)
print(z)  # prints the concatenation of x and y

# or 
# 2 variables
print("version 2")
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)  # prints the sum of x and y

# new formatting for large numbers
print("version 3 - allows floats")
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,.2f}")  # prints the sum of x and y with commas and 2 decimal places

# new rounding for large numbers
print("version 4 - allows floats")
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(z)