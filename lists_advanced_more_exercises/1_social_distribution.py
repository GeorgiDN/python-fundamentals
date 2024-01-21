population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())
count_of_countries = len(population)

if sum(population) < count_of_countries * minimum_wealth:
    print("No equal distribution possible")
else:
    while True:
        if min(population) >= minimum_wealth:
            break
        for idx, country in enumerate(population):
            max_country_index = population.index(max(population))
            if country < minimum_wealth:
                diff = minimum_wealth - country
                population[idx] += diff
                population[max_country_index] -= diff

    print(population)




# population = [int(x) for x in input().split(", ")]
# minimum_wealth = int(input())
# equal_distribution = True

# while True:
#     max_number = max(population)
#     min_number = min(population)

#     difference = minimum_wealth - min_number
#     if max_number - difference < minimum_wealth:
#         print("No equal distribution possible")
#         equal_distribution = False
#         break

#     if min_number >= minimum_wealth:
#         break

#     for idx, number in enumerate(population):
#         max_number = max(population)
#         max_index = population.index(max(population))
#         min_number = min(population)
#         if number < minimum_wealth:
#             diff = minimum_wealth - number
#             if max_number - diff >= minimum_wealth:
#                 population[idx] += diff
#                 population[max_index] -= diff


# if equal_distribution:
#     print(population)
