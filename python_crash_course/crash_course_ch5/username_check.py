current_users = ['admin', 'joesmoe', 'johndoe', 'janedoe', 'jimmyjoe']
new_users = ['admin', 'joesmoe', 'johndoe', 'janedoe', 'hacker1', 'baseballfan94', 'jimmyjoe']

current_users_lower = [user.lower() for user in current_users]
new_users_lower = [user.lower() for user in new_users]

for new_user in new_users_lower:
    if new_user in current_users_lower:
        print(f"Sorry, {new_user} is already taken. Please enter a new username.")
    else:
        print(f"Great! {new_user} is available.")