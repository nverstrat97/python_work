# This program greets users differently based on their username.
# If the username is 'admin', the program will print a special greeting.
usernames = ['admin', 'joesmoe', 'johndoe', 'janedoe', 'jimmyjoe']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    elif username != 'admin':
        print(f"Hello {username}, thank you for logging in again.")
    else:
        print("Username not found.")

if usernames == []:
    print("We need to find some users!")


