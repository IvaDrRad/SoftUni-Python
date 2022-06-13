rows = int(input())
flattened_matrix = []

for _ in range(rows):
    current_row = [int(el) for el in input().split(', ')]
    flattened_matrix.extend(current_row)

print(flattened_matrix)

# used .extend method: The extend() method adds the specified list elements
# (or any iterable) to the end of the current list.