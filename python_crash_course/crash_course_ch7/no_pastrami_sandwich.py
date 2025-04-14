# deli_sandwich.py 
# this program simulates a deli sandwich order system with a loop to process orders and a list to keep track of finished sandwiches - it also limits the orders to not allow pastrami
sandwich_orders = ['reuben', 'BLT', 'pastrami', 'philly cheesesteak', 'tuna salad', 'pastrami', 'turkey']
finished_sandwiches = []
print("The deli has run out of pastrami!")
# remove all pastrami orders from the list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am making your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")