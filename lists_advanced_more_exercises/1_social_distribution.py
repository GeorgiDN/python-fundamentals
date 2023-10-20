def distribute_wealth(population, min_wealth):
    total_wealth = sum(population)
    min_population = len(population) * min_wealth

    if total_wealth < min_population:
        return "No equal distribution possible"

    remaining_wealth = max(population) - min(population)
    population.sort()

    for i in range(len(population)):
        if remaining_wealth <= 0:
            break

        difference = min_wealth - population[i]
        if difference > 0:
            give_wealth = min(difference, remaining_wealth)  # Взимаме по-малкото от необходимото богатство и разликата
            population[i] += give_wealth
            remaining_wealth -= give_wealth
            max_value = max(population)
            max_index = population.index(max_value)
            population[max_index] -= difference

    return population


population = list(map(int, input().split(', ')))
min_wealth = int(input())

result = distribute_wealth(population, min_wealth)
print(result)
