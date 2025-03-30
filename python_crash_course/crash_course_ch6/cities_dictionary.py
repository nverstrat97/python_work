#cities dictionary
cities = {
    'new york': {
        'country': 'united states',
        'population': 8_258_000,
        'fact': 'New York City is known for its iconic landmarks such as the Statue of Liberty and Times Square. It is nicknamed "The Big Apple".',
    },
    'paris': {
        'country': 'france',
        'population': 2_048_000,
        'fact': 'Paris is known for its art, fashion, and culture. It is home to the Eiffel Tower and the Louvre Museum.',
    },
    'tokyo': {
        'country': 'japan',
        'population': 41_000_000,
        'fact': 'Tokyo is known for its modern architecture, bustling streets, and rich history. It is the capital city of Japan and the most populated metropolitan area in the world.',
    },
}

for city in cities:
    city_info = cities[city]
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\n{city.title()} is in {country.title()}.")
    print(f"Population: {population}")
    print(f"Fact: {fact}")