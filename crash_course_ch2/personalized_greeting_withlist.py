# first attempt at using a list to store names and print a personalized greeting
names = ['julianna', 'mike', 'candy', 'aidan', 'zoe', 'emmerson']
# printing first name in list
messageFirst = f"Hello, {names[0].title()}!"
print(messageFirst)
# print last name in list
messageLast = f"Hello, {names[-1].title()}!"
print(messageLast)
# appending list with new name
names.append('luke')
names.append('leia')
print(names)
# removing last two names from list (I know this is not the best way to do this)... I will learn how to do this better later
del names[-1]
del names[-1]
print(names)
