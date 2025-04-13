#movie ticket price program
while True:
    age_input = input("Please enter your age (or 'done' to finish): ")
    if age_input.lower() == 'done':
        print("Thank you for using the ticket price calculator! We are done here.")
        break

    try:
        age = int(age_input)
    except ValueError:
        print("Invalid input. Please enter a number for your age.")
        continue

    if age < 3:
        print("Your ticket is free!")
    elif age < 12:
        print("Your ticket is $10.")
    elif age < 69:
        print("Your ticket is $15.")
    elif age == 69:
        print("Nice Age! Your ticket is free.")
    else:
        print("You're very old. Your ticket is free!")

