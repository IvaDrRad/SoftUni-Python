from collections import deque

working_bees = deque([int(el) for el in input().split()])
nectars = [int(el) for el in input().split()]
honey_making_process = deque(input().split())
total_honey = 0

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

while working_bees and nectars:
    bee = working_bees.popleft()
    nectar = nectars.pop()

    if nectar < bee:
        working_bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    action = honey_making_process.popleft()
    total_honey += abs(operations[action](bee, nectar))

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(bee) for bee in working_bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(nectar) for nectar in nectars])}")


# # 85/100
# from collections import deque
#
# working_bees = deque([int(el) for el in input().split()])
# nectar = [int(el) for el in input().split()]
# honey_making_process = deque(input().split())
# total_honey = 0
#
# operations = {
#     '+': lambda a, b: a + b,
#     '-': lambda a, b: a - b,
#     '*': lambda a, b: a * b,
#     '/': lambda a, b: a / b
# }
#
# while working_bees and nectar:
#     if working_bees[0] > nectar[-1]:
#         nectar.pop()
#     else:
#         action = honey_making_process.popleft()
#         honey = 0
#         honey += operations[action](working_bees.popleft(), nectar.pop())
#         total_honey += abs(honey)
# print(f"Total honey made: {total_honey}")
# if working_bees:
#     print(f"Bees left: {', '.join([str(bee) for bee in working_bees])}")
# if nectar:
#     print(f"Nectar left: {', '.join([str(nectar) for nectar in nectar])}")


