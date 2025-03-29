#list of aliens
aliens = []

#creating 30 green aliens
for alien_number in range(30):
    #creating a new alien
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    #adding the alien to the list of aliens
    aliens.append(new_alien)

#change first three aliens to yellow
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'fast'
#show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
#show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")