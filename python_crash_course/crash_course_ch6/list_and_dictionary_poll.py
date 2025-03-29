favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python'}
polling = ['jen', 'sarah', 'edward', 'phil', 'mike']

# Check for people who have already taken the poll and those who haven't. print appropriate messages.
for person in polling:
    if person in favorite_languages.keys():
        print(f"Thank you {person.title()} for responding.")
    else:
        print(f"{person.title()}, please take the poll.")