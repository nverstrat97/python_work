# examples of string methods
# program asks user for their name and greets them

name = input("What's your name? ")

name = name.strip()  # remove leading and trailing whitespace
print(name)  # print the name with leading and trailing whitespace
name = name.capitalize()  # capitalize the first letter of the string
print(name)  # print the name with the first letter capitalized
name = name.lower()  # convert the string to lowercase
print(name)  # print the name in lowercase
name = name.title()  # convert the string to uppercase  
print(name)  # print the name in uppercase

print(f"hello, {name}")

