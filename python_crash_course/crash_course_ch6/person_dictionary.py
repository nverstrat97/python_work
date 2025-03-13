# This program creates a dictionary with information about a person and then prints out the information. (my first dictionary in python)
dictionary1 = {
    'first_name': 'Nathan',
    'last_name': 'VerStrat',
    'age': 27,
    'city': 'Grand Rapids',
    'state': 'Michigan',
    }

print(dictionary1['first_name'])
print(dictionary1['last_name'])
print(dictionary1['age'])
print(dictionary1['city'])
print(dictionary1['state'])

# favorite numbers
favorite_numbers = {
    'nathan': 27,
    'jake': 4,
    'jessica': 100,
    'josh': 8,
    'jordan': 5,
    }

print(f"Nathan's favorite number is {favorite_numbers['nathan']}.")
print(f"Jake's favorite number is {favorite_numbers['jake']}.")
print(f"Jessica's favorite number is {favorite_numbers['jessica']}.")
print(f"Josh's favorite number is {favorite_numbers['josh']}.")
print(f"Jordan's favorite number is {favorite_numbers['jordan']}.")