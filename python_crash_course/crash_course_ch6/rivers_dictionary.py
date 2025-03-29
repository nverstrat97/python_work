rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china', 'mississippi': 'the united states', 'thames': 'england'}

#this program is a loop through the dictionary and prints the name of the river and the country it runs through.
for name in sorted(rivers.keys()):
    print(f"The {name.title()} runs through {rivers[name].title()}.")