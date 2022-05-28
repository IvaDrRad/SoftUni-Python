number = int(input())
current_row = 0
sum_name = 0
even_nums = set()
odd_nums = set()

for _ in range(number):
    name = input()
    current_row += 1
    for el in name:
        sum_name += ord(el)
    sum_name /= current_row
    if int(sum_name) % 2 == 0:
        even_nums.add(int(sum_name))
    else:
        odd_nums.add(int(sum_name))
    sum_name = 0

final_set = set()
if sum(even_nums) == sum(odd_nums):
    final_set = odd_nums.union(even_nums)
elif sum(even_nums) < sum(odd_nums):
    final_set = odd_nums.difference(even_nums)
else:
    final_set = odd_nums.symmetric_difference(even_nums)

print(', '.join(str(el) for el in final_set))