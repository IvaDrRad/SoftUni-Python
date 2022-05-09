# вариант 1
# def sorted_numbers(list_of_numbers):
#     return sorted(list_of_numbers)   # , reverse=True, ако искаме да е в низходящ ред
#
#
# numbers = input().split()
# numbers_list = []
# for num in numbers:
#     numbers_list.append(int(num))
#
# sort_numbers = sorted_numbers(numbers_list)
# print(sort_numbers)

# вариант 2
result = sorted(list(map(int, input().split())))
print(result)