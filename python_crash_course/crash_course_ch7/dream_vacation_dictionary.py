# a simple program that polls users about their dream vacation destinations
dream_vacation = {}

#set a flag to indicate that polling is active
polling_active = True

while polling_active:
    #ask user for their name and their dream vacation destination
    name = input("\nWhat is your name? ")
    destination = input("If you could visit one place in the world, where would you go? ")

    #store the name and destination in the dictionary
    dream_vacation[name] = destination

    #ask if anyone else wants to take the poll
    repeat = input("Is there anyone else who would like to respond? (yjes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# after poll is complete, show the results
print("\n--- Poll Results ---")
for name, destination in dream_vacation.items():
    print(f"{name.title()} would like to visit {destination.title()}.")