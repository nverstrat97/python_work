# program asks user for their name and greets them

# classic hello world
print("hello world!")
name = input("What's your name? ")

# one argument w/ concatenation
print("hello, " + name)
# two arguments w/ comma (automatically adds space)
print("hello,", name)
# f-string (formatted string literal)
print(f"hello, {name}")