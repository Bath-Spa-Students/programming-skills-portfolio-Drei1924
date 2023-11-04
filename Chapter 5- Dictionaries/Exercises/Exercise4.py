rivers = {
    'Cagayan River': 'Philippines',
    'Shinano River': 'Japan',
    'amazon': 'Brazil'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}.")

# Print the river names
print("\nRiver Names:")
for river in rivers.keys():
    print(river.title())

# Print the countries
print("\nCountries:")
for country in rivers.values():
    print(country)