# Apology letter, deletion
guests = ['Mark Twain', 'Albert Einstein', 'Isaac Newton', 'Marie Curie']

# Here I will remove some of the guests leaving only one remaining. 
while len(guests) > 1:
    guest_pop = guests.pop()
    messageFirst = f"Hello {guest_pop}! I regret to inform you that my big table is broken. I will have to cancel the dinner party, as I can only have one guest at my current table. I am sorry for any inconvenience this may cause."
    print(messageFirst)

# the guest should be empty after this. It will be demonstrated by printing the guest list at the end.
del guests[0]
print(guests)