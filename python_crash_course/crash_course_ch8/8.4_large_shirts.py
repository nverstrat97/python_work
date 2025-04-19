# this program defines a function with a default parameter
def make_shirt(shirt_text, shirt_size="large"):
    # Function to make a shirt with a given size and text
    print(f"Making a {shirt_size} shirt with the text: '{shirt_text}'")

# call the function here with positional arguments
make_shirt('I love Python!')
make_shirt('I love Python!', 'medium')