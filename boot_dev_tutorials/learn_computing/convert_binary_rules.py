'''
Converting Binary
Fantasy Quest needs to migrate old data from strings that look like binary to the integers that the binary strings represent. For example:

"100" -> 4
"101" -> 5
"10010" -> 18
The built-in int() function can convert a binary string to an integer. It takes a second argument that specifies the base of the number (binary is base 2). For example:

# this is a binary string
binary_string = "100"

# convert binary string to integer
num = int(binary_string, 2)
print(num)
# 4

Assignment
Complete the binary_string_to_int function. It takes three binary strings as input and returns each of them in the same order as integers. Each integer is the numerical value of the string when interpreted as binary.

For example:

data_a, data_b, data_c = binary_string_to_int("100", "101", "110")
print(data_a)
# 4
print(data_b)
# 5
print(data_c)
# 6
'''