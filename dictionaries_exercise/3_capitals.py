def find_capitals():
    countries = input().split(", ")
    capitals = input().split(", ")

    counties_with_capitals = {countries[i]: capitals[i] for i in range(len(countries))}
    result = '\n'.join([f"{country} -> {capital} " for country, capital in counties_with_capitals.items()])
    return print(result)


find_capitals()



# countries = input().split(", ")
# capitals = input().split(", ")

# country_capital_dict = {countries[i]: capitals[i] for i in range(len(countries))}

# for country, capital in country_capital_dict.items():
#     print(f"{country} -> {capital}")
  
