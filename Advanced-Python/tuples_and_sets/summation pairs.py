from collections import deque

numbers = deque(input().split())
target = int(input())
counter = 0
pair = []
unique_pair = set()

while len(numbers) > 0:
    for index in range(len(numbers) - 1):
        counter += 1
        if int(numbers[0]) + int(numbers[index + 1]) == target:
            pair.append(int(numbers[0]))
            pair.append(int(numbers[index + 1]))
            pair = tuple(pair)
            unique_pair.add(pair)
            pair = []
            print(f"{int(numbers[0])} + {int(numbers[index + 1])} = {target}")

    numbers.popleft()

print(f"Iterations done: {counter}")
[print(x) for x in unique_pair]


# numbers = list(int(x) for x in input().split())
# target_num = int(input())
# iterations = 1
# unique_pairs = set()
#
# for num1 in range(0, len(numbers)-2):
#     for num2 in range(num1+1, len(numbers)):
#         if numbers[num1] + numbers[num2] == target_num:
#             print(f'{numbers[num1]} + {numbers[num2]} = {target_num}')
#             unique_pairs.add(f'{numbers[num1]}, {numbers[num2]}')
#         iterations += 1
#
# print(f"Iterations done: {iterations}")
# [print(f"({pair})") for pair in unique_pairs]


