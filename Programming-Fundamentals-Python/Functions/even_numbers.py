# вариант 1:
# def list_of_even_numbers(list_of_numbers):
#     even_numbers = list()
#     for digit in numbers:
#         if int(digit) % 2 == 0:
#             even_numbers.append(int(digit))
#     return even_numbers
#
#
# numbers = input().split()
#
# print(list_of_even_numbers(numbers))

# вариант 2:
result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split()))))
print(result)