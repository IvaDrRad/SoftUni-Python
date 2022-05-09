numbers = list(map(int, input().split(', ')))
even_list = []

for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        even_list.append(index)

print(even_list)

# алтернативно решение:
# numbers = list(map(int, input().split(', ')))
# found_index_or_no = map(lambda x: x if numbers[x] % 2 == 0 else 'no', range(len(numbers)))
# even_indices = list(filter(lambda a: a != 'no', found_index_or_no))
# print(even_indices)