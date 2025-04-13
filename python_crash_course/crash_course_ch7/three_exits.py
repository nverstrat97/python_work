# This program demonstrates the use of a while loop to ask the user for their favorite paint colors
paint_colors = []
active = True

while active:
    color = input("Please enter a paint color (or 'done' to finish): ")
    if color.lower() == 'done':
        print("Thank you for using the paint color program! We are done here.")
        break
    else:
        paint_colors.append(color)
        print("Your paint colors are:")
        for color in paint_colors:
            print("- " + color)

        if len(paint_colors) >= 5:
            print("You've reached the maximum number of paint colors. \nThank you for using the paint color program! We are done here.")
            active = False
