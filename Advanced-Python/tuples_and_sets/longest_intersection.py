count = int(input())
set1 = set()
set2 = set()
current_intersection = set()

for _ in range(count):
    first_range, second_range = input().split('-')
    start1, end1 = [int(el) for el in first_range.split(',')]
    start2, end2 = [int(el) for el in second_range.split(',')]
    [set1.add(el) for el in range(start1, end1 + 1)]
    [set2.add(el) for el in range(start2, end2 + 1)]
    new_set = set1.intersection(set2)
    if len(new_set) > len(current_intersection):
        current_intersection = new_set
    set1 = set()
    set2 = set()
print(f"Longest intersection is {list(current_intersection)} with length {len(current_intersection)}")