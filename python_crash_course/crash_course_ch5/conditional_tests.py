# series of conditional tests to reinforce learning

# Test for equality
dog = 'husky'
print("Is dog == 'husky'? I predict True.")
print(dog == 'husky')

print("\nIs dog == 'poodle'? I predict False.")
print(dog == 'poodle')

# Test for inequality
voting_age = 18
print("\nIs voting_age != 18? I predict False.")
print(voting_age != 18)

drinking_age = 21
age = 18
print(f"\nAm I old enough to drink? My age is {age} years old. I predict False.")
print(age >= drinking_age)
if age < 21:
    print("You are not old enough to drink.")
else:
    print("You are old enough to drink")

# Test taking input from user on command line
my_favorite_color = "blue"
user_favorite_color = input("\nWhat is your favorite color? ").strip().lower()

print(f"\nYour favorite color is {user_favorite_color}.")
print(f"My favorite color is {my_favorite_color}.")

if user_favorite_color == my_favorite_color:
    print("We have the same favorite color!")
else:
    print("We do not have the same favorite color.")


