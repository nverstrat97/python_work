# deli_sandwich.py 
# this program simulates a deli sandwich order system with a loop to process orders and a list to keep track of finished sandwiches
sandwich_orders = ['reuben', 'BLT', 'philly cheesesteak', 'tuna salad', 'turkey']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am making your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")