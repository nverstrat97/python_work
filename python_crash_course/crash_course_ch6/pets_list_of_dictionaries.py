sparky = {
    'name': 'Sparky',
    'animal_type': 'dog',
    'owner': 'John',
    'age': 5,
    'weight': 20,
}

fido = {
    'name': 'Fido',
    'animal_type': 'dog',
    'owner': 'Jane',
    'age': 3,
    'weight': 15,
}

whiskers = {
    'name': 'Whiskers',
    'animal_type': 'cat',
    'owner': 'Alice',
    'age': 2,
    'weight': 10,
}
pets = [sparky, fido, whiskers]
for pet in pets:
    print(f"{pet['name']} is a {pet['animal_type']} owned by {pet['owner']}.")
    print(f"{pet['name']} is {pet['age']} years old and weigh {pet['weight']} lbs.\n")