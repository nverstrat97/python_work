# experiments with copying lists and slices
fruit = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

print('The first three items in the list are:')
print(fruit[:3])

print('Three items from the middle of the list are:')
print(fruit[2:5])

print('The last three items in the list are:')
print(fruit[-3:])

pizzas = ['pepperoni', 'cheese', 'deluxe', 'veggie', 'hawaiian']
friend_pizzas = pizzas[:]
pizzas.append('meat lovers')
friend_pizzas.append('margherita')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
# End of script