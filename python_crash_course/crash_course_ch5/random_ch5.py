import random

# List of players
list_of_players = ['mario', 'luigi', 'peach', 'toad', 'yoshi', 'bowser']
# random selection
selected_player = random.choice(list_of_players)
print(f"The selected player is: {selected_player.title()}")
