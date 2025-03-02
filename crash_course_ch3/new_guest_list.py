# This is a program that invites guests to a dinner party and then changes the guest list.
guests = ['Mark Twain', 'Albert Einstein', 'Isaac Newton', 'Marie Curie']
messageFirst = f"Hello, {guests[0].title()}! I would be honored to have you at my dinner party. Please RSVP at your earliest convenience."
print(messageFirst)
messageSecond = f"Hello, {guests[1].title()}! I would be honored to have you at my dinner party. Please RSVP at your earliest convenience."
print(messageSecond)
messageThird = f"Hello, {guests[2].title()}! I would be honored to have you at my dinner party. Please RSVP at your earliest convenience."
print(messageThird)
messageFourth = f"Hello, {guests[3].title()}! I would be honored to have you at my dinner party. Please RSVP at your earliest convenience."
print(messageFourth)
# I could probably make a variable in place of 2 so it is only changed once. I'm leaving as is for now though. 
guestWhoCantMakeIt = guests.pop(2)
print(f"Unfortunately, {guestWhoCantMakeIt.title()} will not be able to attend the dinner party.")
guests.insert(2, 'Nikola Tesla')
messageFifth = f"Hello, {guests[2].title()}! I would be honored to have you at my dinner party. Please RSVP at your earliest convenience."
print(messageFifth)
# found a bigger table. inviting new guests. 
print("I have found a bigger table. I will be inviting more guests.")
guests.insert(0, 'john goodman')
guests.insert(3, 'jackie chan')
guests.append('jim carrey')
# took some research to include everyone from the list in a single message. 
if len(guests) > 1:
    messageSixth = f"Hello, {', '.join([guest.title() for guest in guests[:-1]])}, and {guests[-1].title()}! I would be honored to have you all at my dinner party. Please let me know if you have any food restrictions. Looking forward to seeing you all!"
else:
    messageSixth = f"Hello, {guests[0].title()}! I would be honored to have you at my dinner party. Please let me know if you have any food restrictions. Looking forward to seeing you all!"

print(messageSixth)