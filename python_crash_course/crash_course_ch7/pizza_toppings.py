# this program asks the user for their favorite pizza toppings, adds them to a list, and prints the list
toppings = []
while True:
    topping = input("Please enter a pizza topping (or 'done' to finish): ")
    if topping.lower() == 'done':
        break
    else:
        toppings.append(topping)
        print("Your pizza toppings are:")
        for topping in toppings:
            print("- " + topping)

