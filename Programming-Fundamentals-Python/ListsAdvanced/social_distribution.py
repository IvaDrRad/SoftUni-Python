population_list = list(map(int, input().split(', ')))
min_wealth = int(input())

income_gap = sum([abs(x-min_wealth) for x in population_list if x < min_wealth])
distributable_wealth = sum([abs(x-min_wealth) for x in population_list if x > min_wealth])

if income_gap > distributable_wealth:
    print('No equal distribution possible')
else:
    while min(population_list) < min_wealth:
        wealth_transfer = min_wealth - min(population_list)
        population_list[population_list.index(min(population_list))] += wealth_transfer
        population_list[population_list.index(max(population_list))] -= wealth_transfer

    print(population_list)


# мой вариант, не е дорешен
# population = list(map(int, input().split(", ")))
# min_wealth = int(input())
# not_equal_distribution = False
#
# max_number = max(population)
# numbers_above_wealth = [el for el in population if el > min_wealth]
# index = population.index(max_number)
# wealth_needed = 0
# for num in population:
#     if num < min_wealth:
#         wealth_needed += min_wealth - num
#
# if max_number - wealth_needed >= min_wealth:
#     while population[index] >= min_wealth:
#         population[index] -= min_wealth
#         for el in population:
#             if el < min_wealth:
#                 difference = min_wealth - el
#                 index = population.index(el)
#                 population[index] += difference
#         if population[index] <= min_wealth:
#             print(population)
#             break
# else:
#     if len(numbers_above_wealth) == 0:
#         print("No equal distribution possible")
#     else:
#         while population[index] >= min_wealth:
#             population[index] -= min_wealth
#             for el in population:
#                 if el < min_wealth:
#                     difference = min_wealth - el
#                     index = population.index(el)
#                     population[index] += difference
#         difference = max_number - wealth_needed
#         max_above = max(numbers_above_wealth)
#         index = numbers_above_wealth.index(max_above)
#         numbers_above_wealth.pop(index)
#         max_rest = max(numbers_above_wealth)
#         if max_rest - difference >= min_wealth:
#
#
#         else:
#             while len(numbers_above_wealth) > 0:
#                 index = numbers_above_wealth.index(max_rest)
#                 numbers_above_wealth.pop(index)
#                 if len(numbers_above_wealth) == 0:
#                     print("No equal distribution possible")
#
#
#
