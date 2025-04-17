def make_shirt(shirt_size, shirt_text):
    # Function to make a shirt with a given size and text
    print(f"Making a {shirt_size} shirt with the text: '{shirt_text}'")
# call the function here with positional arguments
make_shirt('large', 'I love Python!')
# call the function here with keyword arguments
make_shirt(shirt_text='I love Python!', shirt_size='large')
