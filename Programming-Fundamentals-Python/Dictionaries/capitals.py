countries = input().split(', ')
cities = input().split(', ')
countries_and_cities = dict(zip(countries, cities))

for k, v in countries_and_cities.items():
    print(f"{k} -> {v}")