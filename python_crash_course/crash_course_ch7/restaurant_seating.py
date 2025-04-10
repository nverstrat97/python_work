#restaurant seating
# 7-2. Restaurant Seating: A restaurant seating program that asks the user how many people are in their party.
# If the party is larger than 7, print a message saying that they will have to wait for a table.
print("Welcome to La Villa Vista!")
party_size = input("How many people are in your party? ")
party_size = int(party_size)
if party_size > 7:
    print("I'm sorry, but you'll have to wait for a table.")
else:
    print("Your table is ready!")
