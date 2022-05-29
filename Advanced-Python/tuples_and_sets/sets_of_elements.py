first_set, second_set = [int(x) for x in input().split()]
first = set()
second = set()

for _ in range(first_set):
    num1 = int(input())
    first.add(num1)

for _ in range(second_set):
    num2 = int(input())
    second.add(num2)

new_set = first.intersection(second)  # ==  first & second
# for new in new_set:
#     print(new)
[print(new) for new in new_set]